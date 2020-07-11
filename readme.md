## 数据迁移
```
python manage.py makemigrations
python manage.py migrate
```

## 上线部署

```python
# myblog settings
DEBUG = False
ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
 创建static文件夹
```shell script
python manage.py collectstatic
```
当django设置为上线模式时，不再提供静态资源服务，该服务由nginx或者apache服务器完成， 因此要添加静态资源路由器
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('account.urls')),
    path('', include('article.urls')),
    path('album/', include('album.urls')),
    path('board/', include('interflow.urls')),
    re_path('media/(?P<path>.*)', serve,
            {'document_root': settings.MEDIA_ROOT}, name='media'),
    re_path('static/(?P<path>.*)', serve,
            {'document_root': settings.STATIC_ROOT}, name='static'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
```

