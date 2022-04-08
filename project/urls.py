# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from django.urls import re_path

from project import views

urlpatterns = [
    re_path(
        r"^get_project/(?P<pk>\d+)/$", views.ProjectViewSet.as_view({"get": "retrieve"})
    ),
    re_path(
        r"^update_project/(?P<pk>\d+)/$",
        views.ProjectViewSet.as_view({"put": "update"}),
    ),
    re_path(
        r"^delete_project/(?P<pk>\d+)/$",
        views.ProjectViewSet.as_view({"delete": "destroy"}),
    ),
    re_path(r"^get_projects/$", views.ProjectViewSet.as_view({"get": "list"})),
    re_path(r"^create_project/$", views.ProjectViewSet.as_view({"post": "create"})),
]
