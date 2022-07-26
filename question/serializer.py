"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版（BLUEKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. ALL rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MII
Unless required by applicable Law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific Language governing permissions and limitations under the License.
"""

from rest_framework import serializers
from question.models import Question
import django_filters
from django_filters.rest_framework import FilterSet

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionShowSerializer(serializers.ModelSerializer):
    types = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = "__all__"

    def get_types(self, data):
        return data.get_types_display()

class QuestionFilter(FilterSet):
    """
    根据title字段的过滤器
    """
    title = django_filters.CharFilter(field_name='title', lookup_expr="icontains")

    class Meta:
        model = Question
        fields = ['title']
