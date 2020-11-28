
from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from jobs import views
import jobs.views
import product.views
from blog import views


#
# from product import views
# from blog import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('django.contrib.auth.urls')),

                  # -------------------------------Blog Page--------------------------
                  path('blog/', views.BlogListView.as_view(), name='blog_list_view'),
                  path('blogdetail/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail_view'),
                  path('createblog/', views.CreateBlog.as_view()),
                  path('updateblog/<int:pk>', views.UpdateBlog.as_view()),
                  path('deleteblog/<int:id>',views.blog_delete_view,name ='blogdelete'),



                            # ----------------Achievement Page(Home Page)------------------------------
                  path('', jobs.views.JobHome.as_view(), name='achievement_page'),
                  path('createachieve/', jobs.views.CreateAchieve.as_view()),
                path('updateachieve/<int:pk>', jobs.views.UpdateAchieve.as_view()),
              path('deleteachieve/<int:id>',jobs.views.job_delete_view,name ='jobtdelete'),



                            # ----------------Project/product Page------------------------------

                  path('product/', product.views.ProductListView.as_view(), name = 'product_list_view'),
                  path('createproduct/',product.views.CreateProduct.as_view()),
                 path('updateproduct/<int:pk>', product.views.UpdateProduct.as_view()),
                path('deleteproduct/<int:id>',product.views.product_delete_view,name ='productdelete'),





              ]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
