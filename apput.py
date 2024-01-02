from flask import Flask, request, jsonify
import re
import pymysql
import json
#http://ec2-13-125-206-239.ap-northeast-2.compute.amazonaws.com:5000

app = Flask(__name__)
#-----------------------------------------------------------------------------------[주거시설(아파트)]-----------------------------------------------------------------------------------
# (if 용도형식:"주거시설(아파트)" 입력한다면)
# (print all 아파트)

# 동양풍 아파트
# (if 건축양식:"전통" and 용도형식:"주거시설(아파트)" 입력한다면)
# (print 전통 아파트)
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
# 빈티지 아파트
# (if 건축양식:"빈티지" and 용도형식:"주거시설(아파트)" 입력한다면)
# (print 빈티지 아파트)
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
# (if 건축양식:"클래식" and 용도형식:"주거시설(아파트)" 입력한다면)
# (print 클래식 아파트)
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
# (if 건축양식:"내츄럴" and 용도형식:"주거시설(아파트)" 입력한다면)
# (print 내츄럴 아파트)
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
# (if 건축양식:"유럽" and 용도형식:"주거시설(아파트)" 입력한다면)
# (print 유럽 아파트)
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
                                        "imageUrl": "https://postfiles.pstatic.net/20160508_222/indian2014_1462692126624az03H_PNG/B8AEBEEEBDBAC5B8C0CF-B5FBB6F3C7CFB0EDBDCDC0BAC0CEC5D7.png?type=w2"
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
# (if 용도형식:"식당(한식)" 입력한다면)
# (print 한식당 인테리어)
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
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/20140902_59/sdindeco_1409644008867R2RUg_JPEG/2014-08-04_11%3B00%3B35.jpg?type=w420"
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
# (if 용도형식:"식당(일식)" or 용도형식:"식당(일본식)" 입력한다면)
# (print 일식당 인테리어)
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
# (if 용도형식:"식당(중식)" 입력한다면)
# (print 중식당 인테리어)
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
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAyMDA0MjNfMTgz/MDAxNTg3NjIzOTU5NjQ1.fjeBKqyYiB2-Ng-WmifhDL2p6fUBilwTIqZkLD6uAMYg.u_8JKG0b7qEb5aAJV8ikhqVcQPc0psgI68HiJfsXe8Ig.JPEG.goodday234/%ED%94%84%EB%9E%9C%EC%B0%A8%EC%9D%B4%EC%A6%88%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_%EC%8B%9D%EB%8B%B9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_%EC%A4%91%EA%B5%AD%EC%A7%91%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_%EC%A4%91%EC%8B%9D%EB%8B%B9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B43.jpg?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/goodday234/221924744743"
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
# (if 용도형식:"식당(양식)" or 용도형식:"식당(레스토랑)" 입력한다면)
# (print 양식당 인테리어)
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

#-----------------------------------------------------------------------------------[카페]-----------------------------------------------------------------------------------

# 동양풍 카페
# (if 건축양식:"전통" and 용도형식:"카페" 입력한다면)
# (print 동양풍 카페)
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
                                    "title": "동양풍 카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAyMTA0MjRfNjQg/MDAxNjE5MjcwNzcwNTU3.pmmZALgvlQ8QtVtAQsDk7lP45ibKufSYplGFn20Md7gg.5FjWlnXsZd4u_FO590fec_nhnzmVlRkEMtLt6uRSLuQg.JPEG.bhj5656/20210424%EF%BC%BF184657.jpg?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/bhj5656/222327727196"
                                        }
                                    ]
                                },
                                {
                                    "title": "동양풍 카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2325/8b9d4011e2b417c5d973398b210cd86f_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2325"
                                        }
                                    ]
                                },
                                {
                                    "title": "동양풍 카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAyMDA0MjlfMzYg/MDAxNTg4MTM3MTAxNzgy.dx2uDDBbKJOcNodabTCwj3hMNKh_jJ6VHHt9pnXu8cgg.rydmVSpco7_-Mz5kpc_WOH_i4AMZCzcZsVHSuG56glsg.JPEG.yeon3314/SE-7c3de57a-de61-4519-be7c-4436bee98e3b.jpg?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/yeon3314/221935993083"
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
# 빈티지 카페
# (if 건축양식:"빈티지" and 용도형식:"카페" 입력한다면)
# (print 빈티지 카페)
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
                                    "title": "빈티지 카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.interiorbay.co.kr/design/upload_file/BD38940/a13d34c22b76052316ea5522fe1da7da_44838_1.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.interiorbay.co.kr/kwa-38941-520?category_3=03"
                                        }
                                    ]
                                },
                                {
                                    "title": "빈티지 카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/139/150b85062b4614fcaa12e70bdeeff562_c800x800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/139"
                                        }
                                    ]
                                },
                                {
                                    "title": "빈티지 카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://ms-housing.kr/data/file/commercial_gallery/2040773419_NoKERhGY_59a7e6d4448e76c158adc52ab5b85674f1e0f829.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=651&sfl=tags&stx=%ED%98%B8%ED%94%84%EC%A7%91%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&page=1&device=pc4"
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
# 클래식 카페
# (if 건축양식:"클래식" and 용도형식:"카페" 입력한다면)
# (print 클래식 카페)
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
                                    "title": "클래식 카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAyMTAzMTlfMiAg/MDAxNjE2MTE2MjgzODkw.Is8zeIKCk5HBoj5ZLQ_6VxpCdyxH7EeDkBUfYVDKzkcg.kR3DDErlPgszMkYr9uDw7VIaaxvWghoH3kSIGKBLvo0g.JPEG.tnalalstn/1616115954912.jpg?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/tnalalstn/222285301095"
                                        }
                                    ]
                                },
                                {
                                    "title": "클래식 카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://postfiles.pstatic.net/MjAyMzAzMDJfMjQ1/MDAxNjc3NzQzMjMzMTE5.LSQ5Wc0Nooq_SH-0VsQsEWX1ohCTcLhJJYftPy_rdxsg.xrGmG7VlF8NVoLJcJRKR1HJe6FHSHSIytm51a4Pf1TMg.JPEG.hycco99/2.jpg?type=w966"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/PostView.naver?blogId=hycco99&logNo=223032726234&parentCategoryNo=&categoryNo=16&viewDate=&isShowPopularPosts=false&from=postView"
                                        }
                                    ]
                                },
                                {
                                    "title": "클래식 카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.interiorbay.co.kr/design/upload_file/BD38940/02d2579f8ebb21477a1bad2aff6a06e8_76495_1.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://interiorbay.co.kr:54306/kwa-38941-740?category_2=01"
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
# 내츄럴 카페
# (if 건축양식:"내츄럴" and 용도형식:"카페" 입력한다면)
# (print 내츄럴 카페)
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
                                    "title": "내츄럴 카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://image.ohou.se/i/bucketplace-v2-development/uploads/projects/cover_images/163358517477585695.jpg?w=1920&h=609&c=c"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://ohou.se/advices/5256"
                                        }
                                    ]
                                },
                                {
                                    "title": "내츄럴 카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAxODA0MTJfMjI5/MDAxNTIzNTE3Mzk5NTUw.oaj0d5INq2CAkvsrQZYKhTQVtLEAL0E3NbZ2bBvnmjgg.L7oI76eoAj2lJv3a22GxQt4IerOWdnJbKD-R_-Xd1ygg.JPEG.allthatseoul/%EC%B9%B4%ED%8E%98%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B417%ED%8F%89.jpg?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/allthatseoul/221251269244"
                                        }
                                    ]
                                },
                                {
                                    "title": "내츄럴 카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.interiorbay.co.kr/design/upload_file/BD38940/366e1facee869cfc57f5be4d6b72a708_78855_1.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.interiorbay.co.kr/kwa-38941-725?category_2=01"
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
# 모던 카페
# (if 건축양식:"모던" and 용도형식:"카페" 입력한다면)
# (print 모던 카페)
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
                                    "title": "모던 카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2237/1ea956cee9df22b278bb3cfe187075dd_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2237"
                                        }
                                    ]
                                },
                                {
                                    "title": "모던 카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1500/21a31cae44b7da2f4ac22eb4e7934e2f_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1500"
                                        }
                                    ]
                                },
                                {
                                    "title": "모던 카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/329/a3b25bd05b3092ffa6da10e8c7c1bf72_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/329"
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
# 유럽풍 카페
# (if 건축양식:"유럽" and 용도형식:"카페" 입력한다면)
# (print 유럽풍 카페)
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
                                    "title": "유럽풍 카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/3705/c4d89ba4b3319c5add71480249bdab27_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/3705"
                                        }
                                    ]
                                },
                                {
                                    "title": "유럽풍 카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://ms-housing.kr/data/file/commercial_gallery/634208394_ykqUaWeQ_ED81ACEAB8B0_15.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=153"
                                        }
                                    ]
                                },
                                {
                                    "title": "유럽풍 카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "http://cp.bbsetheme.com/wp-content/uploads/2014/03/201403211FDD71B8B.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "http://cp.bbsetheme.com/?p=170"
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

#-----------------------------------------------------------------------------------[상가/매장]-----------------------------------------------------------------------------------

# 웨딩샵
# (if 용도형식:"상가/매장(웨딩)" 입력한다면)
# (print 웨딩샵)
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
                                    "title": "웨딩샵",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://cdn.imweb.me/thumbnail/20201218/61b4686350d79.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://interiorgentleman.com/beauty_shop/?idx=401"
                                        }
                                    ]
                                },
                                {
                                    "title": "웨딩샵",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/guide/No.1118-%EC%9B%A8%EB%94%A9%EC%83%B5%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4-%EA%B3%A0%EA%B8%89%EC%8A%A4%EB%9F%AC%EC%9A%B4-60%ED%8F%89-%EB%93%9C%EB%A0%88%EC%8A%A4%EC%83%B5-%EC%99%84%EA%B3%B5-%EC%82%AC%EB%A1%80"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2325"
                                        }
                                    ]
                                },
                                {
                                    "title": "웨딩샵",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://mblogthumb-phinf.pstatic.net/MjAxOTA0MTJfMjEz/MDAxNTU1MDQ4MTQyODc4.bUC63kYReWK1cRQvxX_nJXexJvdUS2ytxZOUpHmQWngg.VCOD1Ozckg4DVpOrkgJwGHWlXva4xwujPmTZ4O5VWvog.JPEG.makewithdesign/20190328_143255.jpg?type=w800"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/makewithdesign/221512012124"
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
# 의류/옷가게
# (if 용도형식:"상가/매장(의류)" or 용도형식:"상가/매장(옷가게)" 입력한다면)
# (print 의류/옷가게)
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
                                    "title": "의류 매장",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1689/a49ef4684b47aa478ccd310e005a1905_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1689"
                                        }
                                    ]
                                },
                                {
                                    "title": "의류 매장",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://ms-housing.kr/data/file/commercial_gallery/31256570_krMOG2Ph_407b084aa2809b44dd5229a5ef427cc686646c5d.png"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=752&sfl=wr_subject||wr_content&stx=%EB%A7%A4%EC%9E%A5&device=pc"
                                        }
                                    ]
                                },
                                {
                                    "title": "의류 매장",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/955/4e484b3691a1a569def562b43ae23a6f_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/955"
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
# 뷰티샵
# (if 용도형식:"상가/매장(뷰티)" 입력한다면)
# (print 뷰티샵)
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
                                    "title": "뷰티샵",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/content/images/2021/08/------------1-2.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/guide/No.1020-%EB%B7%B0%ED%8B%B0%EC%83%B5-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4-20%ED%8F%89-%EB%AA%A8%EB%8D%98-%EC%86%8D%EB%88%88%EC%8D%B9%EC%83%B5"
                                        }
                                    ]
                                },
                                {
                                    "title": "뷰티샵",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.interiorbay.co.kr/design/upload_file/BD38940/e65bbf2d889667945072821db0186db0_55092_1.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.interiorbay.co.kr/kwa-38941-668?category_2=05&frm_page=1&pc=p"
                                        }
                                    ]
                                },
                                {
                                    "title": "뷰티샵",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://ms-housing.kr/data/file/commercial_gallery/1893533933_OE4nYXIe_4b493c9e8102042d8a584fc227411027f13046c1.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=846"
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
# 미용실
# (if 용도형식:"상가/매장(미용실)" 입력한다면)
# (print 미용실)
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
                                    "title": "미용실",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://ms-housing.kr/data/file/commercial_gallery/3068357811_U5giDrb0_c2bc22b1cd2c7cfcc530c73d551dada64a693189.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=950"
                                        }
                                    ]
                                },
                                {
                                    "title": "미용실",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1813/374daec101c967b3eca3401157e7f317_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1813"
                                        }
                                    ]
                                },
                                {
                                    "title": "미용실",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.interiorbay.co.kr/design/upload_file/BD38940/366e1facee869cfc57f5be4d6b72a708_78855_1.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://916er.com/%EC%9E%91%EC%9D%80%EC%86%8C%ED%98%95-%ED%97%A4%EC%96%B4%EC%83%B5-%EC%98%88%EC%81%9C-10%ED%8F%89-%EB%AF%B8%EC%9A%A9%EC%8B%A4%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4/"
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
# 마사지샵
# (if 용도형식:"상가/매장(마사지)" 입력한다면)
# (print 마사지샵)
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
                                    "title": "마사지샵",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2649/d7657380124a63768f2ee3df444c9127_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2649"
                                        }
                                    ]
                                },
                                {
                                    "title": "마사지샵",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://cf.zipdoc.co.kr/static/product/7483/20220222014731175_xotCvxlXUO.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://zipdoc.co.kr/product/detail/index/page?category_cd=20&pid=7483"
                                        }
                                    ]
                                },
                                {
                                    "title": "마사지샵",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.interiorbay.co.kr/design/upload_file/BD38940/%EC%9A%B0%EB%A3%AC%ED%83%80%EC%9D%B4%20(6).jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.interiorbay.co.kr/kwa-38941-156?category_3=05"
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
# 키즈카페
# (if 용도형식:"상가/매장(키즈카페)" 입력한다면)
# (print 키즈카페)
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
                                    "title": "키즈카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/984/23cedd6376aa071bbd1805fd5b6b7227_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/984"
                                        }
                                    ]
                                },
                                {
                                    "title": "키즈카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1202/66537c45208d9b2bf55d16949203135d_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://zipdoc.co.kr/product/detail/index/page?category_cd=20&pid=7483"
                                        }
                                    ]
                                },
                                {
                                    "title": "키즈카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/3000/b241cdd31dc48d08599039188dde9d7a_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/3000"
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
# 애견미용실
# (if 용도형식:"상가/매장(애견미용실)" 입력한다면)
# (print 애견미용실)
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
                                    "title": "애견미용실",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/content/images/2021/08/1-16.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/guide/No.820-15%ED%8F%89-%EC%95%A0%EA%B2%AC%EB%AF%B8%EC%9A%A9%EC%8B%A4%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4-%EC%B9%B4%ED%8E%98%EA%B0%99%EC%9D%80-%EB%B6%84%EC%9C%84%EA%B8%B0"
                                        }
                                    ]
                                },
                                {
                                    "title": "애견미용실",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2404/e83e783d6097fac0ccf55f94ccb96f34_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2404"
                                        }
                                    ]
                                },
                                {
                                    "title": "애견미용실",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1734/74904980576e82608bf5f45fd0f874f2_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1734"
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

#-----------------------------------------------------------------------------------[운동시설]-----------------------------------------------------------------------------------

# 헬스장
# (if {용도형식:"운동시설(운동)" or 용도형식:"운동시설(PT)" or 용도형식:"운동시설(피티)" or 용도형식:"운동시설(헬스)"}입력한다면)
# (print 헬스장)
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
                                    "title": "운동시설",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://ms-housing.kr/data/file/commercial_gallery/3717611045_LEbFBfVS_e2adba647ad4393231a5bbe904de223f927d6bca.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=628"
                                        }
                                    ]
                                },
                                {
                                    "title": "운동시설",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1911/83e3ec5cd7b65b8f08e705ea2b28afb9_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://interiorbay.co.kr:54306/kwa-38941-282?category_3=07&PB_1559696539=2&pc=p"
                                        }
                                    ]
                                },
                                {
                                    "title": "운동시설",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/3299/caddf6891d57c28b6bcc5bbbedbb8fb9_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/3299"
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
# 필라테스
# (if 용도형식:"운동시설(필라테스)" 입력한다면)
# (print 필라테스)
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
                                    "title": "필라테스",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1862/7a5608667ef093e1a5fe69c13430188b_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1862"
                                        }
                                    ]
                                },
                                {
                                    "title": "필라테스",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2926/0dfc68c97538b0c4943bd675a35593f9_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2926"
                                        }
                                    ]
                                },
                                {
                                    "title": "필라테스",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://cf.zipdoc.co.kr/static/item/216738/20230531032916498_QXbFQvuA0P.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://zipdoc.co.kr/product/detail/index/page?category_cd=20&pid=12765"
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
# 요가
# (if 용도형식:"운동시설(요가)" 입력한다면)
# (print 요가)
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
                                    "title": "요가",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/3478/ab244cf11a7feeca257ccfa88e91f7e6_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/3478"
                                        }
                                    ]
                                },
                                {
                                    "title": "요가",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1195/fabbca5a3e9cac06fd3dce87bb7d88d6_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1195"
                                        }
                                    ]
                                },
                                {
                                    "title": "요가",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1322/2092b10b1ee87c89976a894c2931681b_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1322"
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

#-----------------------------------------------------------------------------------[학원(종류)]-----------------------------------------------------------------------------------

# 일반학원
# (if {용도형식:"학원(종류) (국어)" or 용도형식:"학원(종류) (수학)" or 용도형식:"학원(종류) (과학)" or 용도형식:"학원(종류) (영어)"}입력한다면)
# (print 일반학원)
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
                                    "title": "학원",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://cf.zipdoc.co.kr/static/item/137709/20220112143843378_g8LTNgZiIA.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://zipdoc.co.kr/product/detail/index/page?category_cd=20&pid=7163"
                                        }
                                    ]
                                },
                                {
                                    "title": "학원",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1948/e5055b33d8e91985145dd3fafc1e47dd_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1948"
                                        }
                                    ]
                                },
                                {
                                    "title": "학원",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "http://www.designtwoply.com/wp-content/uploads/2020/05/designtwoply0000-2.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "http://www.designtwoply.com/works/ysl-%EC%96%B4%ED%95%99%EC%9B%90-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4/"
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
# 미술학원
# (if 용도형식:"학원(종류) (미술)" 입력한다면)
# (print 미술학원)
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
                                    "title": "미술학원",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/864/85867691a1022861afcddd5ddb75cb0e_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/864"
                                        }
                                    ]
                                },
                                {
                                    "title": "미술학원",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1647/a415b76b673fb10453d591d0becbfa65_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1647"
                                        }
                                    ]
                                },
                                {
                                    "title": "미술학원",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.interiorbay.co.kr/design/upload_file/BD38940/%EC%B2%AD%EB%9D%BC%20%ED%81%B4%EB%A6%AD%20(2).jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.interiorbay.co.kr/kwa-38941-324?category_2=03"
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
# 음악학원
# (if 용도형식:"학원(종류) (음악)" 입력한다면)
# (print 음악학원)
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
                                    "title": "음악학원",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2214/9f4edf7fc074a4eb30d40327b438e79c_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2214"
                                        }
                                    ]
                                },
                                {
                                    "title": "음악학원",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1703/c7b1c84927f6bfb1f864ab2071b6339b_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1703"
                                        }
                                    ]
                                },
                                {
                                    "title": "음악학원",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1637/a4785bec8da5b5d2ea1e0fb56dc95918_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1637"
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
# 태권도장
# (if 용도형식:"학원(종류) (태권도)" 입력한다면)
# (print 태줜도장)
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
                                    "title": "태권도장",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.zipdeco.co.kr/upload/2015/06/05/IMAGE_201506051128176880"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.zipdeco.co.kr/hs/portfolio/imgsearch/View.do?r_seq=3522"
                                        }
                                    ]
                                },
                                {
                                    "title": "태권도장",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "http://www.kukjemat.co.kr/bizdemo34534/component/board/board_2/u_image/25/379989929_1.JPG"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "http://www.kukjemat.co.kr/default/04/01.php?com_board_basic=read_form&com_board_idx=25&&com_board_search_code=&com_board_search_value1=&com_board_search_value2=&com_board_page=&"
                                        }
                                    ]
                                },
                                {
                                    "title": "태권도장",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2956/8c5a3ec30ccea56c2a508ccea5a9f3bf_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2956"
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
# 축구클럽
# (if 용도형식:"학원(종류) (축구)" 입력한다면)
# (print 축구클럽)
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
                                    "title": "축구",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1182/b92f249f7937edeb4ec094ed920f1905_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1182"
                                        }
                                    ]
                                },
                                {
                                    "title": "축구",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://postfiles.pstatic.net/MjAyMjA5MDZfMjk0/MDAxNjYyNDU3NjYzMjA3.kBgWmrI4VPd-ZmfJkJbwCg5Zfk2yW1yQvS5Wa2W4LU8g.KCSqqkMPyUqfJPJr4iwwF4B8APC6kAQrPZ-sMZBK56gg.JPEG.fndlqlqnd/IMG_8122.jpg?type=w966"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/fndlqlqnd/222868583724"
                                        }
                                    ]
                                },
                                {
                                    "title": "축구",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "http://interiorist.co.kr/wp-content/uploads/2019/03/13.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "http://interiorist.co.kr/?project=mom-%EC%B6%95%EA%B5%AC%EA%B5%90%EC%8B%A4"
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
# 스터디카페
# (if 용도형식:"학원(종류) (스터디)" 입력한다면)
# (print 스터디카페)
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
                                    "title": "스터디카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2148/909e1e867c4c9f2a9552f221f8d1bd9c_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2148"
                                        }
                                    ]
                                },
                                {
                                    "title": "스터디카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1683/20fdb8eade6204b31a3328939bd34886_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1683"
                                        }
                                    ]
                                },
                                {
                                    "title": "스터디카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1705/b38d1010c1579f455e7d4946c818b500_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1705"
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

#-----------------------------------------------------------------------------------[사무실]-----------------------------------------------------------------------------------

# 사무실
# (if 용도형식:"사무실" 입력한다면)
# (print 사무실)
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
                                    "title": "사무실",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1739/81dfeadd89fdd82c48345f3c07d6794f_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1739"
                                        }
                                    ]
                                },
                                {
                                    "title": "사무실",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2346/582e79e2a016bfca0fd722329b4b6587_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2346"
                                        }
                                    ]
                                },
                                {
                                    "title": "사무실",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2039/563d082ed2f90b4993f9a6fee7643172_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2039"
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

#-----------------------------------------------------------------------------------[숙박시설]-----------------------------------------------------------------------------------

# 숙박업체
# (if 용도형식:"숙박시설" 입력한다면)
# (print 숙박업체)
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
                                    "title": "숙박시설",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1135/d50a60b3588e071d646b1cfed72252b1_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1135"
                                        }
                                    ]
                                },
                                {
                                    "title": "숙박시설",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://cdn.imweb.me/upload/S201704275901f89d84e04/5b21d7c4ad4ed.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "http://www.zip1004.com/interior/?idx=863088&bmode=view"
                                        }
                                    ]
                                },
                                {
                                    "title": "숙박시설",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://t1.daumcdn.net/thumb/R920x0/?fname=http://zipdeco.co.kr/upload/2023/01/16/EDITOR_202301160251204480_i6IVA"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://interior.realestate.daum.net/asp/story/View.do?lnb=2&mngIdx=1722&category=BBS_TY05_AT01_000008&pageIndex=3"
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

#-----------------------------------------------------------------------------------[병원]-----------------------------------------------------------------------------------

# 치과_인테리어
# (if 용도형식:"병원(치과)" 입력한다면)
# (print 치과_인테리어)
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
                                    "title": "치과_인테리어",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.dailydental.co.kr/data/photos/20220414/art_164915725959_5bbc07.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://zipdoc.co.kr/product/detail/index/page?category_cd=20&pid=7163"
                                        }
                                    ]
                                },
                                {
                                    "title": "치과_인테리어",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1948/e5055b33d8e91985145dd3fafc1e47dd_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1948"
                                        }
                                    ]
                                },
                                {
                                    "title": "치과_인테리어",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "http://www.designtwoply.com/wp-content/uploads/2020/05/designtwoply0000-2.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "http://www.designtwoply.com/works/ysl-%EC%96%B4%ED%95%99%EC%9B%90-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4/"
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
# 미술학원
# (if 용도형식:"병원(미술)" 입력한다면)
# (print 미술학원)
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
                                    "title": "미술학원",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/864/85867691a1022861afcddd5ddb75cb0e_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/864"
                                        }
                                    ]
                                },
                                {
                                    "title": "미술학원",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1647/a415b76b673fb10453d591d0becbfa65_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1647"
                                        }
                                    ]
                                },
                                {
                                    "title": "미술학원",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.interiorbay.co.kr/design/upload_file/BD38940/%EC%B2%AD%EB%9D%BC%20%ED%81%B4%EB%A6%AD%20(2).jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.interiorbay.co.kr/kwa-38941-324?category_2=03"
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
# 음악학원
# (if 용도형식:"병원(음악)" 입력한다면)
# (print 음악학원)
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
                                    "title": "음악학원",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2214/9f4edf7fc074a4eb30d40327b438e79c_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2214"
                                        }
                                    ]
                                },
                                {
                                    "title": "음악학원",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1703/c7b1c84927f6bfb1f864ab2071b6339b_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1703"
                                        }
                                    ]
                                },
                                {
                                    "title": "음악학원",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1637/a4785bec8da5b5d2ea1e0fb56dc95918_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1637"
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
# 태권도장
# (if 용도형식:"병원(태권도)" 입력한다면)
# (print 태줜도장)
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
                                    "title": "태권도장",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.zipdeco.co.kr/upload/2015/06/05/IMAGE_201506051128176880"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.zipdeco.co.kr/hs/portfolio/imgsearch/View.do?r_seq=3522"
                                        }
                                    ]
                                },
                                {
                                    "title": "태권도장",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "http://www.kukjemat.co.kr/bizdemo34534/component/board/board_2/u_image/25/379989929_1.JPG"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "http://www.kukjemat.co.kr/default/04/01.php?com_board_basic=read_form&com_board_idx=25&&com_board_search_code=&com_board_search_value1=&com_board_search_value2=&com_board_page=&"
                                        }
                                    ]
                                },
                                {
                                    "title": "태권도장",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2956/8c5a3ec30ccea56c2a508ccea5a9f3bf_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2956"
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
# 축구클럽
# (if 용도형식:"병원(축구)" 입력한다면)
# (print 축구클럽)
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
                                    "title": "축구",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1182/b92f249f7937edeb4ec094ed920f1905_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1182"
                                        }
                                    ]
                                },
                                {
                                    "title": "축구",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://postfiles.pstatic.net/MjAyMjA5MDZfMjk0/MDAxNjYyNDU3NjYzMjA3.kBgWmrI4VPd-ZmfJkJbwCg5Zfk2yW1yQvS5Wa2W4LU8g.KCSqqkMPyUqfJPJr4iwwF4B8APC6kAQrPZ-sMZBK56gg.JPEG.fndlqlqnd/IMG_8122.jpg?type=w966"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://blog.naver.com/fndlqlqnd/222868583724"
                                        }
                                    ]
                                },
                                {
                                    "title": "축구",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "http://interiorist.co.kr/wp-content/uploads/2019/03/13.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "http://interiorist.co.kr/?project=mom-%EC%B6%95%EA%B5%AC%EA%B5%90%EC%8B%A4"
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
# 스터디카페
# (if 용도형식:"병원(스터디)" 입력한다면)
# (print 스터디카페)
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
                                    "title": "스터디카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2148/909e1e867c4c9f2a9552f221f8d1bd9c_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2148"
                                        }
                                    ]
                                },
                                {
                                    "title": "스터디카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1683/20fdb8eade6204b31a3328939bd34886_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1683"
                                        }
                                    ]
                                },
                                {
                                    "title": "스터디카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1705/b38d1010c1579f455e7d4946c818b500_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1705"
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
# 스터디카페
# (if 용도형식:"병원(스터디)" 입력한다면)
# (print 스터디카페)
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
                                    "title": "스터디카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2148/909e1e867c4c9f2a9552f221f8d1bd9c_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2148"
                                        }
                                    ]
                                },
                                {
                                    "title": "스터디카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1683/20fdb8eade6204b31a3328939bd34886_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1683"
                                        }
                                    ]
                                },
                                {
                                    "title": "스터디카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1705/b38d1010c1579f455e7d4946c818b500_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1705"
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
# 스터디카페
# (if 용도형식:"병원(스터디)" 입력한다면)
# (print 스터디카페)
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
                                    "title": "스터디카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2148/909e1e867c4c9f2a9552f221f8d1bd9c_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2148"
                                        }
                                    ]
                                },
                                {
                                    "title": "스터디카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1683/20fdb8eade6204b31a3328939bd34886_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1683"
                                        }
                                    ]
                                },
                                {
                                    "title": "스터디카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1705/b38d1010c1579f455e7d4946c818b500_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1705"
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
# 스터디카페
# (if 용도형식:"병원(스터디)" 입력한다면)
# (print 스터디카페)
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
                                    "title": "스터디카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2148/909e1e867c4c9f2a9552f221f8d1bd9c_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2148"
                                        }
                                    ]
                                },
                                {
                                    "title": "스터디카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1683/20fdb8eade6204b31a3328939bd34886_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1683"
                                        }
                                    ]
                                },
                                {
                                    "title": "스터디카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1705/b38d1010c1579f455e7d4946c818b500_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1705"
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
# 스터디카페
# (if 용도형식:"병원(스터디)" 입력한다면)
# (print 스터디카페)
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
                                    "title": "스터디카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/2148/909e1e867c4c9f2a9552f221f8d1bd9c_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/2148"
                                        }
                                    ]
                                },
                                {
                                    "title": "스터디카페",
                                    "description": "This is another description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1683/20fdb8eade6204b31a3328939bd34886_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1683"
                                        }
                                    ]
                                },
                                {
                                    "title": "스터디카페",
                                    "description": "This is a description.",
                                    "thumbnail": {
                                        "imageUrl": "https://www.qplace.kr/data/portfolio/1705/b38d1010c1579f455e7d4946c818b500_w800.jpg"
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": "https://www.qplace.kr/portfolio/1705"
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