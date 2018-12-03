# 竞拍项目API V1接口文档



## 首页接口

接口前缀

```python
path('homes/', include('homes.urls')),
```

接口路径

```python
path('index', IndexAPIView.as_view()), # banner 和 topic
path('recommend', RecommendAPIView.as_view()), # 为你推荐
path('guess-you-like', GuessYouLikeAPIView.as_view()), # 猜你喜欢
path('i-am-shooting', IAmShootingAPIView.as_view()), # 我在拍
path('my-collection', MyCollectionAPIView.as_view()), # 我的收藏
```

### 1.index GET

成功请求

``` json
{
    "code": 200,
    "data": {
        "gender": 0,
        "nick": "",
        "oauth_avatar": "",
        "phone": "15913538383",
        "banner": [
            {
                "title": "节省99%的购机优惠，立刻参加",
                "image": "/media/homes/banner/image/apple-iphone-se-press-2.jpg",
                "index": 0,
                "url": null,
                "activity": null,
                "goods": 1
            }
        ],
        "topic": [
            {
                "title": "推荐",
                "icon": "/media/homes/topic/icon/touch.png",
                "index": 0,
                "url": "www.baidu.com",
                "activity": "webcontroller",
                "category": null
            }
        ]
    }
}
```

### 2.为你推荐 GET

返回最热门的商品

```python
Goods.objects.filter(is_hot=True).all()
```

成功请求

``` json
{
    "code": 200,
    "data": [
        {
            "goods_id": "Sxuvm80hRIilw7Jc0nkYzLga5KV1UENn2edkGQIG4cEo9QbpysRf9pDMU5qsjEyi",
            "goods_front_image": "/media/goods/front/image",
            "now_price": 0
        }
    ]
}
```

### 3.猜你喜欢 GET

返回最新加入的商品

```python
Goods.objects.filter(is_new=True).all()
```

成功请求

``` json
{
    "code": 200,
    "data": [
        {
            "goods_id": "Sxuvm80hRIilw7Jc0nkYzLga5KV1UENn2edkGQIG4cEo9QbpysRf9pDMU5qsjEyi",
            "goods_front_image": "/media/goods/front/image",
            "now_price": 0
        }
    ]
}
```

### 4.我在拍 GET

未写



### 5.我的收藏 GET

未写



## 商品接口

接口前缀

```python
path('goods/', include('goods.urls')),
```

接口路径

```python
path('list', GoodsListAPIView.as_view()), # 所有商品
path('detail', GoodsDetailAPIView.as_view()), # 某个商品
path('category/detail', GoodsCategoryDetailAPIView.as_view()), # 某个分类下的商品
path('category/list', GoodsListAPIView.as_view()), # 所有分类的商品
path('news', NewsAPIView.as_view()), # 最新动态
```



### 1.所有商品 GET

成功请求

``` json
{
    "code": 200,
    "data": [
        {
            "category": {
                "name": "十元专区",
                "image": "/media/category/image/",
                "index": 0
            },
            "goods_id": "SAXEUtbqhGWvnd2D7zTAFYOPqw6MW2BU9Jn5mVIM4jQ12oICTEBM2lQg7UzY4OXp",
            "name": "iPhone XS Max",
            "click_num": 0,
            "fav_num": 0,
            "market_price": 9999.99,
            "now_price": 0,
            "goods_brief": "iPhone XS Max",
            "goods_desc": "iPhone XS Max",
            "ship_free": true,
            "goods_front_image": "/media/goods/front/image",
            "is_new": false,
            "is_hot": false,
            "is_sell": false,
            "periods": 1
        },
        {
            "category": {
                "name": "家居生活",
                "image": "/media/category/image/",
                "index": 10
            },
            "goods_id": "Sxuvm80hRIilw7Jc0nkYzLga5KV1UENn2edkGQIG4cEo9QbpysRf9pDMU5qsjEyi",
            "name": "iPhone XS Max",
            "click_num": 0,
            "fav_num": 0,
            "market_price": 9999.99,
            "now_price": 0,
            "goods_brief": "iPhone XS Max",
            "goods_desc": "iPhone XS Max",
            "ship_free": true,
            "goods_front_image": "/media/goods/front/image",
            "is_new": true,
            "is_hot": true,
            "is_sell": false,
            "periods": 1
        }
    ]
}
```

### 2.某个商品 GET

必填参数 

```python
goods_id = request.query_params['goods_id']
```

成功请求

``` json
{
    "code": 200,
    "data": {
        "category": {
            "name": "家居生活",
            "image": "/media/category/image/",
            "index": 10
        },
        "goods_id": "Sxuvm80hRIilw7Jc0nkYzLga5KV1UENn2edkGQIG4cEo9QbpysRf9pDMU5qsjEyi",
        "name": "iPhone XS Max",
        "click_num": 0,
        "fav_num": 0,
        "market_price": 9999.99,
        "now_price": 0,
        "goods_brief": "iPhone XS Max",
        "goods_desc": "iPhone XS Max",
        "ship_free": true,
        "goods_front_image": "/media/goods/front/image",
        "is_new": true,
        "is_hot": true,
        "is_sell": false,
        "periods": 1,
        "goods_images": []
    }
}
```

### 3.某个分类下的商品 GET

必填参数

```python
category_id = request.query_params['category_id']
```

成功请求

``` json
{
    "code": 200,
    "data": [
        {
            "goods_id": "SAXEUtbqhGWvnd2D7zTAFYOPqw6MW2BU9Jn5mVIM4jQ12oICTEBM2lQg7UzY4OXp",
            "name": "iPhone XS Max",
            "click_num": 0,
            "fav_num": 0,
            "market_price": 9999.99,
            "now_price": 0,
            "goods_brief": "iPhone XS Max",
            "goods_desc": "iPhone XS Max",
            "ship_free": true,
            "goods_front_image": "/media/goods/front/image",
            "is_new": false,
            "is_hot": false,
            "is_sell": false,
            "periods": 1
        },
        {
            "goods_id": "IP5U9O9TujKwxV4zVbyQ9EcQry9Jngalb83S2YXo3YezmlfG1Ck1E4KfaS1oxmvl",
            "name": "iPhone XS Max",
            "click_num": 0,
            "fav_num": 0,
            "market_price": 9999.99,
            "now_price": 0,
            "goods_brief": "iPhone XS Max",
            "goods_desc": "iPhone XS Max",
            "ship_free": true,
            "goods_front_image": "/media/goods/front/image",
            "is_new": false,
            "is_hot": false,
            "is_sell": false,
            "periods": 1
        },
        {
            "goods_id": "VEPESQGiZpeLwrHqg2LQaCD2UAVccxeDU3nha9J93cqzbGwk3o1FRguTEse04GEM",
            "name": "iPhone XS Max",
            "click_num": 0,
            "fav_num": 0,
            "market_price": 9999.99,
            "now_price": 0,
            "goods_brief": "iPhone XS Max",
            "goods_desc": "iPhone XS Max",
            "ship_free": true,
            "goods_front_image": "/media/goods/front/image",
            "is_new": false,
            "is_hot": false,
            "is_sell": false,
            "periods": 1
        }
    ]
}
```

### 4.所有分类的商品 GET

成功请求：

​	所有商品



## 用户接口

接口前缀

```python
path('users/', include('users.urls')),
```

接口路径

```python
path('phone/login', PhoneLogin.as_view()),  # 手机登录
path('phone/register', PhoneRegister.as_view()),  # 手机注册
path('info', InfoAPIView.as_view()),  # 用户信息
path('token-refresh', refresh_jwt_token),  # 刷新token
```

### 1. 手机登录接口 POST

必填参数:

```python
phone = request.data['phone']
password = request.data['password']
```

成功请求:

``` json
{
    "code": 200,
    "data": {
        "gender": 0,
        "nick": "",
        "oauth_avatar": "",
        "phone": "15913538383",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6Ilx1NjI0Ylx1NjczYVx1NzUyOFx1NjIzNzE1OTEzNTM4MzgzIiwiZXhwIjoxNTQxOTIwODkwLCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNTQxMzE2MDkwfQ.ncPphcRKO6nCc6I1CUvS_dEq0zEDLDi-APrt2EnsTMk"
    },
    "msg": "登录成功"
}
```

### 2.手机注册接口 POST

必填参数:

``` python
phone = request.data['phone']
password = request.data['password']
code = request.data['code'] # 短信验证码，开发环境填入66666
platform = request.data['platform']
```

成功请求:

``` json
{
    "code": 200,
    "data": {
        "gender": 0,
        "nick": "",
        "oauth_avatar": "",
        "phone": "15913538384",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6Ilx1NjI0Ylx1NjczYVx1NzUyOFx1NjIzNzE1OTEzNTM4Mzg0IiwiZXhwIjoxNTQxOTIxMDY2LCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNTQxMzE2MjY2fQ.H_7WH3IEk2mH-_OG0QHUKOZdSuv2pC11Ig6GC_u1eJA"
    },
    "msg": "注册成功"
}
```

### 3.用户信息 GET

成功请求:

``` json
{
    "code": 200,
    "data": {
        "gender": 0,
        "nick": "",
        "oauth_avatar": "",
        "phone": "15913538383"
    }
}
```

### 4.刷新token POST

必填参数：

``` python
token = request.data['token']
```



成功请求:

``` json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6Ilx1NjI0Ylx1NjczYVx1NzUyOFx1NjIzNzE1OTEzNTM4MzgzIiwiZXhwIjoxNTQxOTIxOTE1LCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNTQxMzE2MDkwfQ.bgMaqhfxV_aZS68exvLOts5A60snB8yEtyxPVNTlHr8"
}
```





## 用户操作接口





## 消息接口

