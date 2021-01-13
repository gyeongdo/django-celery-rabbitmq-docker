from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from datetime import datetime, timedelta
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

from .tasks import *


# def send_email(request):
#     subject = '[Data-ON] 문의하신 사항에 대해 답변드립니다.​'
#     text_content = 'ttttttttttttttt'
#     # html_content = request.data['email_content']
#
#     email_obj = {
#         "question_type": request.data['question_type'],
#         "question": request.data['question_content'],
#         "answer": request.data['email_content'],
#     }
#
#     html_content = render_to_string("email_confirmation_message.html", {"email_obj": email_obj})
#     to = [request.data['email']]
#     from_email = 'sales@openmate-on.co.kr'
#
#     email = EmailMultiAlternatives(subject, text_content, from_email, to)
#     email.attach_alternative(html_content, "text/html")
#     print('@@@@@@@@ sent')
#     result = email.send()


class PollsViewSet(ModelViewSet):
    serializer_class = TblistInquireInsertSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = TblistInquire.objects.all()

    def retrieve(self, request, pk=None):
        queryset = TblistInquire.objects.get(pk=pk)
        serializer = TblistInquireSerializer(queryset)

        add.delay(1, 5)

        return Response(serializer.data)
