from flask import Flask, request, jsonify
import re
import pymysql
import json
#http://ec2-13-125-206-239.ap-northeast-2.compute.amazonaws.com:5000

app = Flask(__name__)
## 동양풍 아파트
@app.route('/api/east_house', methods=['POST'])
def east_house():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "동양풍 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.zipdeco.co.kr/upload/2018/11/19/IMAGE_201811191141191290_JHWbP"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.zipdeco.co.kr/hs/portfolio/imgsearch/View.do?r_seq=6682"
                                        }
                                    ]
                                },
                                {
                                    "title": "동양풍 아파트",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://image.ohou.se/i/bucketplace-v2-development/uploads/cards/projects/167342942753363463.jpeg?w=720"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://contents.ohou.se/projects/135460"
                                        }
                                    ]
                                },
                                {
                                    "title": "동양풍 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.womansense.co.kr/upload/woman/article/202004/thumb/44688-409506-sample.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.womansense.co.kr/woman/article/44688"
                                        }
                                    ]
                                } 
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500
# 한국풍 아파트
@app.route('/api/hanok_house', methods=['POST'])
def hanok_house():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "한옥풍 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://images.homify.com/c_fill,f_auto,h_500,q_auto,w_1280/v1509716467/p/photo/image/2301899/wdsin_10.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/loratiger/221097324315"
                                        }
                                    ]
                                },
                                {
                                    "title": "한옥풍 아파트",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://dev-archisketch-resources.s3.ap-northeast-2.amazonaws.com/seesoop/v2/Interiorideas_HJ/1630906327_3.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.seesoop.com/interior-idea/__2b0d3151-ea05-43dd-9880-f427cd4b6d6e"
                                        }
                                    ]
                                },
                                {
                                    "title": "한옥풍 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://i1.daumcdn.net/cfile80/image/99BC36485B8E4071313996"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://board.realestate.daum.net/gaia/do/estate/power/read?bbsId=power&articleId=2515"
                                        }
                                    ]
                                } 
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500
# 일본풍 아파트
@app.route('/api/japan_house', methods=['POST'])
def japan_house():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "일본풍 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F998AC1485AA6326936"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://gamemaster5.tistory.com/116"
                                        }
                                    ]
                                },
                                {
                                    "title": "일본풍 아파트",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAxNzAzMzFfMTg2/MDAxNDkwOTM5MTQ2NjE0.QTPeJuKYQ_20JU0sUch28jzffoNlqu_PsKzSGsk6Djgg.fv0N3j_YgGVsGCgLJTyK1E6A7g9SkXDQB4UUCdxP3TIg.JPEG.hesogood/%EA%B0%80%EA%B5%AC%EC%9D%98%EC%9E%90%EB%A6%AC331-5.JPG?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/lolliathome/220971808250"
                                        }
                                    ]
                                },
                                {
                                    "title": "일본풍 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://post-phinf.pstatic.net/MjAxNzAyMThfMTIx/MDAxNDg3MzcxOTI3MjI0.CxfXcOfHxCj3mK0T-nWcDTQhj_JpdWCrjOt8l3TApeMg.qtNRf1kPDzBx6SMxrC6q1IRVupwI9Cg15tOMFnPgjoMg.JPEG/mug_obj_201702180752075493.jpg?type=w1080"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://post.naver.com/viewer/postView.nhn?memberNo=392639&volumeNo=6538196&vType=VERTICAL"
                                        }
                                    ]
                                } 
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

# 빈티지 아파트
@app.route('/api/retro_house', methods=['POST'])
def retro_house():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "빈티지 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://blog.kakaocdn.net/dn/drWjA7/btrexloVA2k/v9xuQJcu4fH90IIIq7NI9k/img.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://thefltnblack.tistory.com/entry/%EB%A0%88%ED%8A%B8%EB%A1%9C%ED%95%98%EA%B2%8C-%EA%BE%B8%EB%AF%BC-32%ED%8F%89%EC%95%84%ED%8C%8C%ED%8A%B8%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4"
                                        }
                                    ]
                                },
                                {
                                    "title": "빈티지 아파트",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAxNzA1MzFfMjQw/MDAxNDk2MjA4NzIxNDMz.J5a6rHtPz38WiMTDrP-4BjlWM7Qco3WcCvYdhRSd604g.ZPLLFLuVakWRKTsacv4S8x8PPsloqAgyH17-T40rVlwg.JPEG.h31122/1940s-Retro-Apartment-Renovations-Palacio-5E-in-Porto-by-Atelier-in-vitro-Yellowtrace-01.jpg?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/h31122/221018516576"
                                        }
                                    ]
                                },
                                {
                                    "title": "빈티지 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://images.homify.com/v1495266928/p/photo/image/2021086/%EA%B1%B0%EC%8B%A413.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.homify.co.kr/ideabooks/4169325/%EB%A0%88%ED%8A%B8%EB%A1%9C-%EA%B0%90%EC%84%B1%EC%9D%98-43%ED%8F%89-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4"
                                        }
                                    ]
                                } 
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500
# 클래식 아파트
@app.route('/api/classic_house', methods=['POST'])
def classic_house():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "클래식 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.zipdeco.co.kr/upload/2019/07/02/EDITOR_201907021035147840_r78u7"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.zipdeco.co.kr/hs/story/View.do?mngIdx=1480&category="
                                        }
                                    ]
                                },
                                {
                                    "title": "클래식 아파트",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.zipdeco.co.kr/upload/2019/05/16/EDITOR_201905161102098920_lY668"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.zipdeco.co.kr/hs/story/View.do?category=&mngIdx=1452"
                                        }
                                    ]
                                },
                                {
                                    "title": "클래식 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.interiorbay.co.kr/design/upload_file/BD39007/358643add9c77b8c0fd5f08a1eb64f97_14009_1.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.interiorbay.co.kr/kwa-39008-59?category_3=05&pc=p"
                                        }
                                    ]
                                } 
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500
# 내츄럴 아파트
@app.route('/api/netural_house', methods=['POST'])
def netural_house():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "내츄럴 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1JxmrqhNX5eGULNAbAM7Dhnom4tG09FvFJA&usqp=CAU"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://m.blog.naver.com/jh_kkang/221044293163"
                                        }
                                    ]
                                },
                                {
                                    "title": "내츄럴 아파트",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://blog.kakaocdn.net/dn/bvunnx/btrlQ1K4qGC/zs49MxkzyutNGKOHxr8Gc0/img.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://thefltnblack.tistory.com/661"
                                        }
                                    ]
                                },
                                {
                                    "title": "내츄럴 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://i1.daumcdn.net/cfile245/image/2275A33A55ED0E9E19CF54"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://board.realestate.daum.net/gaia/do/estate/knowHow/read?bbsId=knowhow&articleId=175308"
                                        }
                                    ]
                                } 
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500
# 유럽풍 아파트
@app.route('/api/europe_house', methods=['POST'])
def europe_house():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "유럽풍 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "data:image/jpeg;base64,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"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/indian2014/220704158614"
                                        }
                                    ]
                                },
                                {
                                    "title": "유럽풍 아파트",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://post-phinf.pstatic.net/MjAxOTA2MTBfMjMg/MDAxNTYwMTQ2NDM5OTI4.KnGjWmBNt3Nd0nMXHKYk6oR83pyJFF6Ej1P8J9OzSC0g.vvEyK4BesTWdOV7fSycb6c0waIYAZNYXOldK9TE6X9Ig.JPEG/00_%EB%A9%94%EC%9D%B8.jpg?type=w1200"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://post.naver.com/viewer/postView.nhn?volumeNo=21037556&memberNo=15864193&searchKeyword=%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&searchRank=27"
                                        }
                                    ]
                                },
                                {
                                    "title": "유럽풍 아파트",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://t1.daumcdn.net/cfile/tistory/99A02D355E57AEAE09"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://thefltnblack.tistory.com/223"
                                        }
                                    ]
                                } 
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500
#-----------------------------------------------------------------------------------[식당]-----------------------------------------------------------------------------------

# 한식당 인테리어
@app.route('/api/kr_res', methods=['POST'])
def kor_kres():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "한식당 인테리어",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "data:image/jpeg;base64,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"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/sdindeco/220111206410"
                                        }
                                    ]
                                },
                                {
                                    "title": "한식당 인테리어",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAyMzA1MTFfMjE1/MDAxNjgzNzYzNTQ3ODI5.T11RVlVO6PhqGkIunxX4N-08zDZ6zFoxybo8LtrCM1kg.ZC50K8dQwZm-O8HVkLtTHB6vYcM4NrqJCfHnH15IFpog.JPEG.bbee1119/batch_IMG_5965.JPG?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/bbee1119/223099027634"
                                        }
                                    ]
                                },
                                {
                                    "title": "한식당 인테리어",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "http://www.newspeople.co.kr/news/upload/1693530200167_c.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "http://www.newspeople.co.kr/news_view.jsp?ncd=46962"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

# 일식당 인테리어
@app.route('/api/jp_res', methods=['POST'])
def japan_house():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "일식당 인테리어",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAxODExMTVfMjI4/MDAxNTQyMjY1NjgxMjk4.qqJeMyQyJwFnobBXCoWVaYCEt7vSpDsUD1vpzCH9Lssg.4gVBWTQgHQQXwOLiz0tCWJ4Nlv6lEEC_4T7wk82b1lAg.JPEG.allthatseoul/2._%EC%9D%BC%EC%8B%9D%EC%A7%91_%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4.jpg?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/allthatseoul/221399346174"
                                        }
                                    ]
                                },
                                {
                                    "title": "일식당 인테리어",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAxNzAzMzFfMTg2/MDAxNDkwOTM5MTQ2NjE0.QTPeJuKYQ_20JU0sUch28jzffoNlqu_PsKzSGsk6Djgg.fv0N3j_YgGVsGCgLJTyK1E6A7g9SkXDQB4UUCdxP3TIg.JPEG.hesogood/%EA%B0%80%EA%B5%AC%EC%9D%98%EC%9E%90%EB%A6%AC331-5.JPG?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/sdindeco/220496524223"
                                        }
                                    ]
                                },
                                {
                                    "title": "일식당 인테리어",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAyMDA1MTNfMjUy/MDAxNTg5MzU3NzQzNzA3.cnDHJRVQi1yfV-AgP-3lthf9jnYYBtIrniryFmEC3qcg.VwBsK1Y5dWX9cJnL87R42ifjfK4jYZphaeA5bQNKoigg.JPEG.goodday234/%EC%8A%A4%EC%8B%9C%EC%A7%91%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_%EC%B4%88%EB%B0%A5%EC%A7%91%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_%EC%83%81%EA%B0%80%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B44.jpg?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/goodday234/221960782544"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

# 중식당 인테리어
@app.route('/api/ch_res', methods=['POST'])
def ch_res():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "중식당 인테리어",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAxOTAxMjNfMjI2/MDAxNTQ4MjIwMTQwMTk0.1IxUQZT9XEVkS84_lkWDEnYPbMiyRNadG88eAzr6IVEg.DjgE15a-wr7sn-xXE-rtuV61UhpMsfuv2zmQ3YNe9bog.JPEG.canny464/%EC%A4%91%EA%B5%AD%EC%A7%91_%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_(1).jpg?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/canny464/221449197631"
                                        }
                                    ]
                                },
                                {
                                    "title": "중식당 인테리어",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2222/35fd9c7adbce5ec142feec4c289bc1bd_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2222"
                                        }
                                    ]
                                },
                                {
                                    "title": "중식당 인테리어",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "data:image/jpeg;base64,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"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=sdindeco&logNo=220748019337"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

# 양식당 인테리어
@app.route('/api/eu_res', methods=['POST'])
def eu_res():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "양식당 인테리어",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://interiorbay.co.kr:54306/design/upload_file/BD38940/%EC%97%90%EC%8A%90%EB%A6%AC%20%EC%88%98%EC%9B%90%20(2).jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://interiorbay.co.kr:54306/kwa-38941-340?category_3=04&pc=p"
                                        }
                                    ]
                                },
                                {
                                    "title": "양식당 인테리어",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://t1.daumcdn.net/cfile/tistory/2780B733597AF93A06"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://goodchoice-interior.tistory.com/entry/%EC%A2%8B%EC%9D%80-%EB%B6%84%EC%9C%84%EA%B8%B0%EC%97%90%EC%84%9C-%EC%96%91%EC%8B%9D%EC%9D%84-%EB%A8%B9%EA%B3%A0-%EC%8B%B6%EC%9D%84%EB%95%8C-%EB%A0%88%EC%8A%A4%ED%86%A0%EB%9E%91-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4"
                                        }
                                    ]
                                },
                                {
                                    "title": "양식당 인테리어",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://ms-housing.kr/data/file/commercial_gallery/3068357811_Muwp0TzW_bf6461d01ca1c629de541dbe2a47d5a54c6c9cb9.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=1291&sfl=tags&stx=%EB%A6%AC%EC%B9%98%EC%95%88%ED%83%80%EC%9B%8C%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&sop=or&device=pc"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5032, debug=True)