from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RecAIResponse, FertAIResponse
from .serializers import RecAIResponseSerializer, FertAIResponseSerializer
from scripts.scripts import get_ai_response 

class RecAIResponseView(APIView):
    """
    Handles creating and rating AI responses for recommendations.
    """

    def post(self, request):
        """
        Process AI prompt and save the response.
        """
        data = request.data
        user = request.user
        answer = get_ai_response(**data, user_id=user.id)
        response = RecAIResponse.objects.create(user=user, answer=answer, **data)
        return Response(RecAIResponseSerializer(response).data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        """
        Update the answer rating for a specific response.
        """
        response = RecAIResponse.objects.filter(id=pk).first()
        if not response:
            return Response({"detail": "Response not found"}, status=status.HTTP_404_NOT_FOUND)
        response.answer_rating = request.data.get("answer_rating")
        response.save()
        return Response({"detail": "Rating updated successfully"}, status=status.HTTP_200_OK)


class FertAIResponseView(APIView):
    """
    Handles creating and rating fertilizer-related AI responses.
    """
    def post(self, request):
        """
        Process AI prompt and save the fertilizer response.
        """
        data = request.data
        user = request.user
        answer = get_ai_response(**data, user_id=user.id)
        response = FertAIResponse.objects.create(user=user, answer=answer, **data)
        return Response(FertAIResponseSerializer(response).data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        """
        Update the answer rating for a specific fertilizer response.
        """
        response = FertAIResponse.objects.filter(id=pk).first()
        if not response:
            return Response({"detail": "Response not found"}, status=status.HTTP_404_NOT_FOUND)
        response.answer_rating = request.data.get("answer_rating")
        response.save()
        return Response({"detail": "Rating updated successfully"}, status=status.HTTP_200_OK)
