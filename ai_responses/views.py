import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import RecAIResponse, FertAIResponse
from .serializers import RecAIResponseSerializer, FertAIResponseSerializer
from scripts.scripts import  get_crop_ai_response, get_fertilizer_response
from users.models import UserInfo  


class RecAIResponseView(APIView):
    """
    Handles creating and rating AI responses for recommendations.
    """

    def post(self, request):
        """
        Process AI prompt and save the response.
        Expects JSON like:
        {
          "user": 1,
          "nitrogen": 45.2,
          "phosphorus": 34.1,
          "potassium": 20.5,
          "temperature": 30.1,
          "humidity": 40.2,
          "ph": 6.5,
          "rainfall": 120.3,
          "session_id": 12345
        }
        """
        data = request.data

        # 1. Get the user ID from the request data
        user_id = data.get("user")
        if not user_id:
            return Response(
                {"detail": "A valid 'user' ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 2. Convert that user_id into a UserInfo instance
        user_info = get_object_or_404(UserInfo, pk=user_id)

        # 3. Remove 'user' from the data to avoid assigning an integer to the FK
        cleaned_data = data.copy()
        cleaned_data.pop("user", None)

        # 4. Generate the AI answer
        answer = get_crop_ai_response(**cleaned_data, user_id=user_id)

        # 5. Create the RecAIResponse object with the user instance
        response_obj = RecAIResponse.objects.create(
            user=user_info,
            answer=answer,
            **cleaned_data
        )

        return Response(
            RecAIResponseSerializer(response_obj).data, 
            status=status.HTTP_201_CREATED
        )

    def patch(self, request, pk):
        """
        Update the answer rating for a specific response.
        Expects JSON like:
        {
          "answer_rating": 4.5
        }
        """
        response_obj = RecAIResponse.objects.filter(id=pk).first()
        if not response_obj:
            return Response({"detail": "Response not found"}, status=status.HTTP_404_NOT_FOUND)

        response_obj.answer_rating = request.data.get("answer_rating")
        response_obj.save()
        return Response({"detail": "Rating updated successfully"}, status=status.HTTP_200_OK)



from rest_framework import status

class FertAIResponseView(APIView):
    """
    Handles creating and rating fertilizer-related AI responses.
    """

    def post(self, request):
        """
        Process AI prompt and save the fertilizer response.
        Expects JSON like:
        {
          "user": 1,
          "nitrogen": 45.2,
          "phosphorus": 34.1,
          "potassium": 20.5,
          "temperature": 30.1,
          "humidity": 40.2,
          "moisture": 15.5,
          "crop_type": 1,
          "soil_type": 0,
          "session_id": 12345
        }
        """
        data = request.data

        # 1. Get the user ID from the request data
        user_id = data.get("user")
        if not user_id:
            return Response(
                {"detail": "A valid 'user' ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_info = get_object_or_404(UserInfo, pk=user_id)

        cleaned_data = data.copy()
        cleaned_data.pop("user", None)
        answer = get_fertilizer_response(**cleaned_data, user_id=user_id)

        # 5. Create the FertAIResponse object with the user instance
        response_obj = FertAIResponse.objects.create(
            user=user_info,
            answer=answer,
            **cleaned_data
        )

        return Response(
            FertAIResponseSerializer(response_obj).data,
            status=status.HTTP_201_CREATED
        )

    def patch(self, request, pk):
        """
        Update the answer rating for a specific fertilizer response.
        Expects JSON like:
        {
          "answer_rating": 4
        }
        """
        response_obj = FertAIResponse.objects.filter(id=pk).first()
        if not response_obj:
            return Response({"detail": "Response not found"}, status=status.HTTP_404_NOT_FOUND)

        response_obj.answer_rating = request.data.get("answer_rating")
        response_obj.save()
        return Response({"detail": "Rating updated successfully"}, status=status.HTTP_200_OK)
