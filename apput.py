from flask import Flask, request, jsonify
import re
import pymysql
import json
#http://ec2-13-125-206-239.ap-northeast-2.compute.amazonaws.com:5000

app = Flask(__name__)

#-----------------------------------------------------------------------------------[주거시설(아파트)]-----------------------------------------------------------------------------------

@app.route('/api/sayHello', methods=['GET'])
def hello():
    return "자동응답"


@app.route('/api/apartment', methods=['POST'])
def apartment():
    try:
        form = request.json.get('action', {}).get('detailParams', {}).get('스타일', {}).get('value', '')
        use = request.json.get('action', {}).get('detailParams', {}).get('용도형식', {}).get('value', '')
        
        if(form=="전통" and use == "아파트"):
            title = "동양풍"
            description = title + "스타일 인테리어입니다"
            
            imageURL1 = "https://www.zipdeco.co.kr/upload/2018/11/19/IMAGE_201811191141191290_JHWbP"
            imageURL2 = "https://image.ohou.se/i/bucketplace-v2-development/uploads/cards/projects/167342942753363463.jpeg?w=720"
            imageURL3 = "https://www.womansense.co.kr/upload/woman/article/202004/thumb/44688-409506-sample.jpg"
            
            webLinkUrl1 = "https://www.zipdeco.co.kr/hs/portfolio/imgsearch/View.do?r_seq=6682"
            webLinkUrl2 = "https://contents.ohou.se/projects/135460"
            webLinkUrl3 = "https://www.womansense.co.kr/woman/article/44688"
        
        elif(form=="빈티지" and use == "아파트"):
            title = "빈티지"
            description = title + "스타일 인테리어입니다"
            
            imageURL1 = "https://blog.kakaocdn.net/dn/drWjA7/btrexloVA2k/v9xuQJcu4fH90IIIq7NI9k/img.jpg"
            imageURL2 = "https://mblogthumb-phinf.pstatic.net/MjAxNzA1MzFfMjQw/MDAxNDk2MjA4NzIxNDMz.J5a6rHtPz38WiMTDrP-4BjlWM7Qco3WcCvYdhRSd604g.ZPLLFLuVakWRKTsacv4S8x8PPsloqAgyH17-T40rVlwg.JPEG.h31122/1940s-Retro-Apartment-Renovations-Palacio-5E-in-Porto-by-Atelier-in-vitro-Yellowtrace-01.jpg?type=w800"
            imageURL3 = "https://images.homify.com/v1495266928/p/photo/image/2021086/%EA%B1%B0%EC%8B%A413.jpg"
            
            webLinkUrl1 = "https://thefltnblack.tistory.com/entry/%EB%A0%88%ED%8A%B8%EB%A1%9C%ED%95%98%EA%B2%8C-%EA%BE%B8%EB%AF%BC-32%ED%8F%89%EC%95%84%ED%8C%8C%ED%8A%B8%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4"
            webLinkUrl2 = "https://blog.naver.com/h31122/221018516576"
            webLinkUrl3 = "https://www.homify.co.kr/ideabooks/4169325/%EB%A0%88%ED%8A%B8%EB%A1%9C-%EA%B0%90%EC%84%B1%EC%9D%98-43%ED%8F%89-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4"
            
        elif(form=="클래식" and use == "아파트"):
            title = "클래식"
            description = title + "스타일 인테리어입니다"
            
            imageURL1 = "https://www.zipdeco.co.kr/upload/2019/07/02/EDITOR_201907021035147840_r78u7"
            imageURL2 = "https://www.zipdeco.co.kr/upload/2019/05/16/EDITOR_201905161102098920_lY668"
            imageURL3 = "https://www.interiorbay.co.kr/design/upload_file/BD39007/358643add9c77b8c0fd5f08a1eb64f97_14009_1.jpg"
            
            webLinkUrl1 = "https://www.zipdeco.co.kr/hs/story/View.do?mngIdx=1480&category="
            webLinkUrl2 = "https://www.zipdeco.co.kr/hs/story/View.do?category=&mngIdx=1452"
            webLinkUrl3 = "https://www.interiorbay.co.kr/kwa-39008-59?category_3=05&pc=p"
            
        elif(form=="내츄럴" and use == "아파트"):
            title = "내츄럴"
            description = title + "스타일 인테리어입니다"
            
            imageURL1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1JxmrqhNX5eGULNAbAM7Dhnom4tG09FvFJA&usqp=CAU"
            imageURL2 = "https://blog.kakaocdn.net/dn/bvunnx/btrlQ1K4qGC/zs49MxkzyutNGKOHxr8Gc0/img.jpg"
            imageURL3 = "https://i1.daumcdn.net/cfile245/image/2275A33A55ED0E9E19CF54"
            
            webLinkUrl1 = "https://m.blog.naver.com/jh_kkang/221044293163"
            webLinkUrl2 = "https://thefltnblack.tistory.com/661"
            webLinkUrl3 = "https://board.realestate.daum.net/gaia/do/estate/knowHow/read?bbsId=knowhow&articleId=175308"
        
        elif(form=="유럽" and use == "아파트"):
            title = "유럽풍"
            description = title + "스타일 인테리어입니다"
            
            imageURL1 = "https://postfiles.pstatic.net/20160508_222/indian2014_1462692126624az03H_PNG/B8AEBEEEBDBAC5B8C0CF-B5FBB6F3C7CFB0EDBDCDC0BAC0CEC5D7.png?type=w2"
            imageURL2 = "https://post-phinf.pstatic.net/MjAxOTA2MTBfMjMg/MDAxNTYwMTQ2NDM5OTI4.KnGjWmBNt3Nd0nMXHKYk6oR83pyJFF6Ej1P8J9OzSC0g.vvEyK4BesTWdOV7fSycb6c0waIYAZNYXOldK9TE6X9Ig.JPEG/00_%EB%A9%94%EC%9D%B8.jpg?type=w1200"
            imageURL3 = "https://t1.daumcdn.net/cfile/tistory/99A02D355E57AEAE09"
            
            
            webLinkUrl1 = "https://blog.naver.com/indian2014/220704158614"
            webLinkUrl2 = "https://post.naver.com/viewer/postView.nhn?volumeNo=21037556&memberNo=15864193&searchKeyword=%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&searchRank=27"
            webLinkUrl3 = "https://thefltnblack.tistory.com/223"

        elif(use == "아파트"):
            title = "아파트"
            description = title + " 인테리어입니다"
            
            imageURL1 = "https://www.zipdeco.co.kr/upload/2018/11/19/IMAGE_201811191141191290_JHWbP"
            imageURL2 = "https://mblogthumb-phinf.pstatic.net/MjAxNzA1MzFfMjQw/MDAxNDk2MjA4NzIxNDMz.J5a6rHtPz38WiMTDrP-4BjlWM7Qco3WcCvYdhRSd604g.ZPLLFLuVakWRKTsacv4S8x8PPsloqAgyH17-T40rVlwg.JPEG.h31122/1940s-Retro-Apartment-Renovations-Palacio-5E-in-Porto-by-Atelier-in-vitro-Yellowtrace-01.jpg?type=w800"
            imageURL3 = "https://www.zipdeco.co.kr/upload/2019/05/16/EDITOR_201905161102098920_lY668"
            imageURL4 = "https://blog.kakaocdn.net/dn/bvunnx/btrlQ1K4qGC/zs49MxkzyutNGKOHxr8Gc0/img.jpg"
            imageURL5 = "https://t1.daumcdn.net/cfile/tistory/99A02D355E57AEAE09"
            
            webLinkUrl1 = "https://www.zipdeco.co.kr/hs/portfolio/imgsearch/View.do?r_seq=6682"
            webLinkUrl2 = "https://blog.naver.com/h31122/221018516576"
            webLinkUrl3 = "https://www.zipdeco.co.kr/hs/story/View.do?category=&mngIdx=1452"
            webLinkUrl4 = "https://thefltnblack.tistory.com/661"
            webLinkUrl5 = "https://thefltnblack.tistory.com/223"
            
        else:
            simpleText = "죄송합니다. 다시 입력해주세요"
        
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL1
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl1
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL2
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl2
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL3
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl3
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL4
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl4
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL5
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl5
                                        }
                                    ]
                                },
                                {
                                    "title": "네?",
                                    "description": simpleText,
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": ""
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        print(request.get_json())
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

#-----------------------------------------------------------------------------------[식당]-----------------------------------------------------------------------------------

@app.route('/api/restaurant', methods=['POST'])
def restaurant():
    try:
        use = request.json.get('action', {}).get('detailParams', {}).get('용도형식', {}).get('value', '')
        
        if(use=="한식"):
            title = "한식당"
            description = title + " 인테리어입니다"
            
            imageURL1 = "https://mblogthumb-phinf.pstatic.net/20140902_59/sdindeco_1409644008867R2RUg_JPEG/2014-08-04_11%3B00%3B35.jpg?type=w420"
            imageURL2 = "https://mblogthumb-phinf.pstatic.net/MjAyMzA1MTFfMjE1/MDAxNjgzNzYzNTQ3ODI5.T11RVlVO6PhqGkIunxX4N-08zDZ6zFoxybo8LtrCM1kg.ZC50K8dQwZm-O8HVkLtTHB6vYcM4NrqJCfHnH15IFpog.JPEG.bbee1119/batch_IMG_5965.JPG?type=w800"
            imageURL3 = "http://www.newspeople.co.kr/news/upload/1693530200167_c.jpg"
            
            webLinkUrl1 = "https://blog.naver.com/sdindeco/220111206410"
            webLinkUrl2 = "https://blog.naver.com/bbee1119/223099027634"
            webLinkUrl3 = "http://www.newspeople.co.kr/news_view.jsp?ncd=46962"
        
        elif(use=="중식"):
            title = "중식당"
            description = title + " 인테리어입니다"
            
            imageURL1 = "https://mblogthumb-phinf.pstatic.net/MjAxOTAxMjNfMjI2/MDAxNTQ4MjIwMTQwMTk0.1IxUQZT9XEVkS84_lkWDEnYPbMiyRNadG88eAzr6IVEg.DjgE15a-wr7sn-xXE-rtuV61UhpMsfuv2zmQ3YNe9bog.JPEG.canny464/%EC%A4%91%EA%B5%AD%EC%A7%91_%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_(1).jpg?type=w800"
            imageURL2 = "https://www.qplace.kr/data/portfolio/2222/35fd9c7adbce5ec142feec4c289bc1bd_w800.jpg"
            imageURL3 = "https://mblogthumb-phinf.pstatic.net/MjAyMDA0MjNfMTgz/MDAxNTg3NjIzOTU5NjQ1.fjeBKqyYiB2-Ng-WmifhDL2p6fUBilwTIqZkLD6uAMYg.u_8JKG0b7qEb5aAJV8ikhqVcQPc0psgI68HiJfsXe8Ig.JPEG.goodday234/%ED%94%84%EB%9E%9C%EC%B0%A8%EC%9D%B4%EC%A6%88%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_%EC%8B%9D%EB%8B%B9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_%EC%A4%91%EA%B5%AD%EC%A7%91%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_%EC%A4%91%EC%8B%9D%EB%8B%B9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B43.jpg?type=w800"
            
            webLinkUrl1 = "https://blog.naver.com/canny464/221449197631"
            webLinkUrl2 = "https://www.qplace.kr/portfolio/2222"
            webLinkUrl3 = "https://blog.naver.com/goodday234/221924744743"
            
        elif(use=="일식"):
            title = "일식당"
            description = title + " 인테리어입니다"
            
            imageURL1 = "https://mblogthumb-phinf.pstatic.net/MjAxODExMTVfMjI4/MDAxNTQyMjY1NjgxMjk4.qqJeMyQyJwFnobBXCoWVaYCEt7vSpDsUD1vpzCH9Lssg.4gVBWTQgHQQXwOLiz0tCWJ4Nlv6lEEC_4T7wk82b1lAg.JPEG.allthatseoul/2._%EC%9D%BC%EC%8B%9D%EC%A7%91_%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4.jpg?type=w800"
            imageURL2 = "https://mblogthumb-phinf.pstatic.net/MjAxNzAzMzFfMTg2/MDAxNDkwOTM5MTQ2NjE0.QTPeJuKYQ_20JU0sUch28jzffoNlqu_PsKzSGsk6Djgg.fv0N3j_YgGVsGCgLJTyK1E6A7g9SkXDQB4UUCdxP3TIg.JPEG.hesogood/%EA%B0%80%EA%B5%AC%EC%9D%98%EC%9E%90%EB%A6%AC331-5.JPG?type=w800"
            imageURL3 = "https://mblogthumb-phinf.pstatic.net/MjAyMDA1MTNfMjUy/MDAxNTg5MzU3NzQzNzA3.cnDHJRVQi1yfV-AgP-3lthf9jnYYBtIrniryFmEC3qcg.VwBsK1Y5dWX9cJnL87R42ifjfK4jYZphaeA5bQNKoigg.JPEG.goodday234/%EC%8A%A4%EC%8B%9C%EC%A7%91%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_%EC%B4%88%EB%B0%A5%EC%A7%91%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_%EC%83%81%EA%B0%80%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B44.jpg?type=w800"
            
            webLinkUrl1 = "https://blog.naver.com/allthatseoul/221399346174"
            webLinkUrl2 = "https://blog.naver.com/sdindeco/220496524223"
            webLinkUrl3 = "https://blog.naver.com/goodday234/221960782544"
            
        elif(use=="양식"):
            title = "양식당"
            description = title + " 인테리어입니다"
            
            imageURL1 = "https://interiorbay.co.kr:54306/design/upload_file/BD38940/%EC%97%90%EC%8A%90%EB%A6%AC%20%EC%88%98%EC%9B%90%20(2).jpg"
            imageURL2 = "https://t1.daumcdn.net/cfile/tistory/2780B733597AF93A06"
            imageURL3 = "https://ms-housing.kr/data/file/commercial_gallery/3068357811_Muwp0TzW_bf6461d01ca1c629de541dbe2a47d5a54c6c9cb9.jpg"
            
            webLinkUrl1 = "https://interiorbay.co.kr:54306/kwa-38941-340?category_3=04&pc=p"
            webLinkUrl2 = "https://goodchoice-interior.tistory.com/entry/%EC%A2%8B%EC%9D%80-%EB%B6%84%EC%9C%84%EA%B8%B0%EC%97%90%EC%84%9C-%EC%96%91%EC%8B%9D%EC%9D%84-%EB%A8%B9%EA%B3%A0-%EC%8B%B6%EC%9D%84%EB%95%8C-%EB%A0%88%EC%8A%A4%ED%86%A0%EB%9E%91-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4"
            webLinkUrl3 = "https://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=1291&sfl=tags&stx=%EB%A6%AC%EC%B9%98%EC%95%88%ED%83%80%EC%9B%8C%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&sop=or&device=pc"
        
        else:
            simpleText = "죄송합니다. 다시 입력해주세요"
            
            
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL1
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl1
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL2
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl2
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL3
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl3
                                        }
                                    ]
                                },
                                {
                                    "title": "네?",
                                    "description": simpleText,
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": ""
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        print(request.get_json())
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500
    
#-----------------------------------------------------------------------------------[카페]-----------------------------------------------------------------------------------

@app.route('/api/cafe', methods=['POST'])
def cafe():
    try:
        form = request.json.get('action', {}).get('detailParams', {}).get('스타일', {}).get('value', '')
        use = request.json.get('action', {}).get('detailParams', {}).get('용도형식', {}).get('value', '')
        
        if(form=="전통" and use == "카페"):
            title = "동양풍"
            description = title + "스타일 카페 인테리어입니다"
            
            imageURL1 = "https://mblogthumb-phinf.pstatic.net/MjAyMTA0MjRfNjQg/MDAxNjE5MjcwNzcwNTU3.pmmZALgvlQ8QtVtAQsDk7lP45ibKufSYplGFn20Md7gg.5FjWlnXsZd4u_FO590fec_nhnzmVlRkEMtLt6uRSLuQg.JPEG.bhj5656/20210424%EF%BC%BF184657.jpg?type=w800"
            imageURL2 = "https://www.qplace.kr/data/portfolio/2325/8b9d4011e2b417c5d973398b210cd86f_w800.jpg"
            imageURL3 = "https://mblogthumb-phinf.pstatic.net/MjAyMDA0MjlfMzYg/MDAxNTg4MTM3MTAxNzgy.dx2uDDBbKJOcNodabTCwj3hMNKh_jJ6VHHt9pnXu8cgg.rydmVSpco7_-Mz5kpc_WOH_i4AMZCzcZsVHSuG56glsg.JPEG.yeon3314/SE-7c3de57a-de61-4519-be7c-4436bee98e3b.jpg?type=w800"
            
            webLinkUrl1 = "https://blog.naver.com/bhj5656/222327727196"
            webLinkUrl2 = "https://www.qplace.kr/portfolio/2325"
            webLinkUrl3 = "https://blog.naver.com/yeon3314/221935993083"
        
        elif(form=="빈티지" and use == "카페"):
            title = "빈티지"
            description = title + "스타일 카페 인테리어입니다"
            
            imageURL1 = "https://www.interiorbay.co.kr/design/upload_file/BD38940/a13d34c22b76052316ea5522fe1da7da_44838_1.jpg"
            imageURL2 = "https://www.qplace.kr/data/portfolio/139/150b85062b4614fcaa12e70bdeeff562_c800x800.jpg"
            imageURL3 = "https://ms-housing.kr/data/file/commercial_gallery/2040773419_NoKERhGY_59a7e6d4448e76c158adc52ab5b85674f1e0f829.jpg"
            
            webLinkUrl1 = "https://www.interiorbay.co.kr/kwa-38941-520?category_3=03"
            webLinkUrl2 = "https://www.qplace.kr/portfolio/139"
            webLinkUrl3 = "https://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=651&sfl=tags&stx=%ED%98%B8%ED%94%84%EC%A7%91%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4&page=1&device=pc4"
            
        elif(form=="클래식" and use == "카페"):
            title = "클래식"
            description = title + "스타일 카페 인테리어입니다"
            
            imageURL1 = "https://mblogthumb-phinf.pstatic.net/MjAyMTAzMTlfMiAg/MDAxNjE2MTE2MjgzODkw.Is8zeIKCk5HBoj5ZLQ_6VxpCdyxH7EeDkBUfYVDKzkcg.kR3DDErlPgszMkYr9uDw7VIaaxvWghoH3kSIGKBLvo0g.JPEG.tnalalstn/1616115954912.jpg?type=w800"
            imageURL2 = "https://postfiles.pstatic.net/MjAyMzAzMDJfMjQ1/MDAxNjc3NzQzMjMzMTE5.LSQ5Wc0Nooq_SH-0VsQsEWX1ohCTcLhJJYftPy_rdxsg.xrGmG7VlF8NVoLJcJRKR1HJe6FHSHSIytm51a4Pf1TMg.JPEG.hycco99/2.jpg?type=w966"
            imageURL3 = "https://www.interiorbay.co.kr/design/upload_file/BD38940/02d2579f8ebb21477a1bad2aff6a06e8_76495_1.jpg"
            
            webLinkUrl1 = "https://blog.naver.com/tnalalstn/222285301095"
            webLinkUrl2 = "https://blog.naver.com/PostView.naver?blogId=hycco99&logNo=223032726234&parentCategoryNo=&categoryNo=16&viewDate=&isShowPopularPosts=false&from=postView"
            webLinkUrl3 = "https://interiorbay.co.kr:54306/kwa-38941-740?category_2=01"
            
        elif(form=="내츄럴" and use == "카페"):
            title = "내츄럴"
            description = title + "스타일 카페 인테리어입니다"
            
            imageURL1 = "https://image.ohou.se/i/bucketplace-v2-development/uploads/projects/cover_images/163358517477585695.jpg?w=1920&h=609&c=c"
            imageURL2 = "https://mblogthumb-phinf.pstatic.net/MjAxODA0MTJfMjI5/MDAxNTIzNTE3Mzk5NTUw.oaj0d5INq2CAkvsrQZYKhTQVtLEAL0E3NbZ2bBvnmjgg.L7oI76eoAj2lJv3a22GxQt4IerOWdnJbKD-R_-Xd1ygg.JPEG.allthatseoul/%EC%B9%B4%ED%8E%98%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B417%ED%8F%89.jpg?type=w800"
            imageURL3 = "https://www.interiorbay.co.kr/design/upload_file/BD38940/366e1facee869cfc57f5be4d6b72a708_78855_1.jpg"
            
            webLinkUrl1 = "https://ohou.se/advices/5256"
            webLinkUrl2 = "https://blog.naver.com/allthatseoul/221251269244"
            webLinkUrl3 = "https://www.interiorbay.co.kr/kwa-38941-725?category_2=01"
        
        elif(form=="모던" and use == "카페"):
            title = "모던"
            description = title + "스타일 카페 인테리어입니다"
            
            imageURL1 = "https://www.qplace.kr/data/portfolio/2237/1ea956cee9df22b278bb3cfe187075dd_w800.jpg"
            imageURL2 = "https://www.qplace.kr/data/portfolio/1500/21a31cae44b7da2f4ac22eb4e7934e2f_w800.jpg"
            imageURL3 = "https://www.qplace.kr/data/portfolio/329/a3b25bd05b3092ffa6da10e8c7c1bf72_w800.jpg"
            
            webLinkUrl1 = "https://www.qplace.kr/portfolio/2237"
            webLinkUrl2 = "https://www.qplace.kr/portfolio/1500"
            webLinkUrl3 = "https://www.qplace.kr/portfolio/329"
        
        elif(form=="유럽" and use == "카페"):
            title = "유럽풍"
            description = title + "스타일 카페 인테리어입니다"
            
            imageURL1 = "https://www.qplace.kr/data/portfolio/3705/c4d89ba4b3319c5add71480249bdab27_w800.jpg"
            imageURL2 = "https://ms-housing.kr/data/file/commercial_gallery/634208394_ykqUaWeQ_ED81ACEAB8B0_15.jpg"
            imageURL3 = "http://cp.bbsetheme.com/wp-content/uploads/2014/03/201403211FDD71B8B.jpg"
            
            webLinkUrl1 = "https://www.qplace.kr/portfolio/3705"
            webLinkUrl2 = "https://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=153"
            webLinkUrl3 = "http://cp.bbsetheme.com/?p=170"

        elif(use == "카페"):
            title = "카페"
            description = title + " 인테리어입니다"
            
            imageURL1 = "https://www.qplace.kr/data/portfolio/2325/8b9d4011e2b417c5d973398b210cd86f_w800.jpg"
            imageURL2 = "https://www.qplace.kr/data/portfolio/139/150b85062b4614fcaa12e70bdeeff562_c800x800.jpg"
            imageURL3 = "https://www.interiorbay.co.kr/design/upload_file/BD38940/02d2579f8ebb21477a1bad2aff6a06e8_76495_1.jpg"
            imageURL4 = "https://www.interiorbay.co.kr/design/upload_file/BD38940/366e1facee869cfc57f5be4d6b72a708_78855_1.jpg"
            imageURL5 = "https://www.qplace.kr/data/portfolio/2237/1ea956cee9df22b278bb3cfe187075dd_w800.jpg"
            imageURL6 = "https://www.qplace.kr/data/portfolio/3705/c4d89ba4b3319c5add71480249bdab27_w800.jpg"
            
            webLinkUrl1 = "https://www.qplace.kr/portfolio/2325"
            webLinkUrl2 = "https://www.qplace.kr/portfolio/139"
            webLinkUrl3 = "https://interiorbay.co.kr:54306/kwa-38941-740?category_2=01"
            webLinkUrl4 = "https://www.interiorbay.co.kr/kwa-38941-725?category_2=01"
            webLinkUrl5 = "https://www.qplace.kr/portfolio/2237"
            webLinkUrl6 = "https://www.qplace.kr/portfolio/3705"
            
        else:
            simpleText = "죄송합니다. 다시 입력해주세요"
        
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL1
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl1
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL2
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl2
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL3
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl3
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL4
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl4
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL5
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl5
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL6
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl6
                                        }
                                    ]
                                },
                                {
                                    "title": "네?",
                                    "description": simpleText,
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": ""
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        print(request.get_json())
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

#-----------------------------------------------------------------------------------[상가/매장]-----------------------------------------------------------------------------------

@app.route('/api/shop', methods=['POST'])
def shop():
    try:
        use = request.json.get('action', {}).get('detailParams', {}).get('용도형식', {}).get('value', '')
        
        if(use=="상가/매장"):
            title = "여러가지 상가, 매장의"
            description = title + " 인테리어입니다"
            imageURL1 = "https://www.qplace.kr/data/portfolio/1118/bf8e0d28300d265bb5acae996303c8ab_w800.jpg"
            imageURL2 = "https://www.qplace.kr/data/portfolio/1689/a49ef4684b47aa478ccd310e005a1905_w800.jpg"
            imageURL3 = "https://www.qplace.kr/data/portfolio/1020/81bc82583ddb0cec7e0c6f403149cba1_w800.jpg"
            imageURL4 = "https://www.qplace.kr/data/portfolio/1813/374daec101c967b3eca3401157e7f317_w800.jpg"
            imageURL5 = "https://www.qplace.kr/data/portfolio/2649/d7657380124a63768f2ee3df444c9127_w800.jpg"
            imageURL6 = "https://www.qplace.kr/data/portfolio/984/23cedd6376aa071bbd1805fd5b6b7227_w800.jpg"
            imageURL7 = "https://www.qplace.kr/data/portfolio/1734/74904980576e82608bf5f45fd0f874f2_w800.jpg"
            
            webLinkUrl1 = "https://www.qplace.kr/portfolio/1118"
            webLinkUrl2 = "https://www.qplace.kr/portfolio/1689"
            webLinkUrl3 = "https://www.qplace.kr/portfolio/1020"
            webLinkUrl4 = "https://www.qplace.kr/portfolio/1813"
            webLinkUrl5 = "https://www.qplace.kr/portfolio/2649"
            webLinkUrl6 = "https://www.qplace.kr/portfolio/984"
            webLinkUrl7 = "https://www.qplace.kr/portfolio/1734"
        
        else:
            simpleText = "죄송합니다. 다시 입력해주세요"
            
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "웨딩홀",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL1
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl1
                                        }
                                    ]
                                },
                                {
                                    "title": "의류 매장",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL2
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl2
                                        }
                                    ]
                                },
                                {
                                    "title": "뷰티샵",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL3
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl3
                                        }
                                    ]
                                },
                                {
                                    "title": "미용실",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL4
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl4
                                        }
                                    ]
                                },
                                {
                                    "title": "마사지샵",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL5
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl5
                                        }
                                    ]
                                },
                                {
                                    "title": "키즈카페",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL6
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl6
                                        }
                                    ]
                                },
                                {
                                    "title": "애견미용실",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL7
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl7
                                        }
                                    ]
                                },
                                {
                                    "title": "네?",
                                    "description": simpleText,
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": ""
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        print(request.get_json())
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

#-----------------------------------------------------------------------------------[운동시설]-----------------------------------------------------------------------------------

@app.route('/api/exercise', methods=['POST'])
def exercise():
    try:
        use = request.json.get('action', {}).get('detailParams', {}).get('용도형식', {}).get('value', '')
        
        if(use=="운동시설"):
            title = "운동시설"
            description = title + "의 인테리어입니다"
            
            imageURL1 = "https://ms-housing.kr/data/file/commercial_gallery/3717611045_LEbFBfVS_e2adba647ad4393231a5bbe904de223f927d6bca.jpghttps://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=628"
            imageURL2 = "https://www.qplace.kr/data/portfolio/1911/83e3ec5cd7b65b8f08e705ea2b28afb9_w800.jpg"
            imageURL3 = "https://www.qplace.kr/data/portfolio/3299/caddf6891d57c28b6bcc5bbbedbb8fb9_w800.jpg"
            
            webLinkUrl1 = "https://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=628"
            webLinkUrl2 = "https://www.qplace.kr/portfolio/1911"
            webLinkUrl3 = "https://www.qplace.kr/portfolio/3299"
        
        else:
            simpleText = "죄송합니다. 다시 입력해주세요"
            
            
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL1
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl1
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL2
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl2
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL3
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl3
                                        }
                                    ]
                                },
                                {
                                    "title": "네?",
                                    "description": simpleText,
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": ""
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        print(request.get_json())
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

#-----------------------------------------------------------------------------------[학원]-----------------------------------------------------------------------------------

@app.route('/api/academy', methods=['POST'])
def academy():
    try:
        use = request.json.get('action', {}).get('detailParams', {}).get('용도형식', {}).get('value', '')
        
        if(use=="학원"):
            
            title = "여러가지 학원의"
            description = title + " 인테리어입니다"
            imageURL1 = "https://www.qplace.kr/data/portfolio/3375/453543adc412a3d63aece14656e84bd8_w800.jpg"
            imageURL2 = "https://www.qplace.kr/data/portfolio/1948/e5055b33d8e91985145dd3fafc1e47dd_w800.jpg"
            imageURL3 = "https://www.qplace.kr/data/portfolio/4133/94bfba9c4c9e50463f3e300b1f09f1d4_w800.jpg"
            imageURL4 = "https://www.qplace.kr/data/portfolio/1481/7c232dd47e88304b2578f34ad2da1395_w800.jpg"
            imageURL5 = "https://www.qplace.kr/data/portfolio/2214/e475ccda458447f0d560c254550eb448_w800.jpg"
            imageURL6 = "https://www.qplace.kr/data/portfolio/864/85867691a1022861afcddd5ddb75cb0e_w800.jpg"
            
            webLinkUrl1 = "https://www.qplace.kr/portfolio/3375"
            webLinkUrl2 = "https://www.qplace.kr/portfolio/1948"
            webLinkUrl3 = "https://www.qplace.kr/portfolio/4133"
            webLinkUrl4 = "https://www.qplace.kr/portfolio/1481"
            webLinkUrl5 = "https://www.qplace.kr/portfolio/2214"
            webLinkUrl6 = "https://www.qplace.kr/portfolio/864"
        
        else:
            simpleText = "죄송합니다. 다시 입력해주세요"
            
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "국어학원",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL1
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl1
                                        }
                                    ]
                                },
                                {
                                    "title": "수학학원",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL2
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl2
                                        }
                                    ]
                                },
                                {
                                    "title": "과학학원",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL3
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl3
                                        }
                                    ]
                                },
                                {
                                    "title": "영어학원",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL4
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl4
                                        }
                                    ]
                                },
                                {
                                    "title": "음악학원",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL5
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl5
                                        }
                                    ]
                                },
                                {
                                    "title": "미술학원",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL6
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl6
                                        }
                                    ]
                                },
                                {
                                    "title": "네?",
                                    "description": simpleText,
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": ""
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        print(request.get_json())
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

#-----------------------------------------------------------------------------------[사무실]-----------------------------------------------------------------------------------

@app.route('/api/office', methods=['POST'])
def office():
    try:
        use = request.json.get('action', {}).get('detailParams', {}).get('용도형식', {}).get('value', '')
        
        if(use=="사무실"):
            title = "사무실"
            description = title + "의 인테리어입니다"
            
            imageURL1 = "https://www.qplace.kr/data/portfolio/1739/81dfeadd89fdd82c48345f3c07d6794f_w800.jpg"
            imageURL2 = "https://www.qplace.kr/data/portfolio/2346/582e79e2a016bfca0fd722329b4b6587_w800.jpg"
            imageURL3 = "https://www.qplace.kr/data/portfolio/2039/563d082ed2f90b4993f9a6fee7643172_w800.jpg"
            
            webLinkUrl1 = "https://www.qplace.kr/portfolio/1739"
            webLinkUrl2 = "https://www.qplace.kr/portfolio/2346"
            webLinkUrl3 = "https://www.qplace.kr/portfolio/2039"
        
        else:
            simpleText = "죄송합니다. 다시 입력해주세요"
            
            
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL1
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl1
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL2
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl2
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL3
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl3
                                        }
                                    ]
                                },
                                {
                                    "title": "네?",
                                    "description": simpleText,
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": ""
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        print(request.get_json())
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

#-----------------------------------------------------------------------------------[숙박시설]-----------------------------------------------------------------------------------

@app.route('/api/hotel', methods=['POST'])
def hotel():
    try:
        use = request.json.get('action', {}).get('detailParams', {}).get('용도형식', {}).get('value', '')
        
        if(use=="숙박시설"):
            title = "숙박시설"
            description = title + "의 인테리어입니다"
            
            imageURL1 = "https://www.qplace.kr/data/portfolio/1135/d50a60b3588e071d646b1cfed72252b1_w800.jpg"
            imageURL2 = "https://cdn.imweb.me/upload/S201704275901f89d84e04/5b21d7c4ad4ed.jpg"
            imageURL3 = "https://t1.daumcdn.net/thumb/R920x0/?fname=http://zipdeco.co.kr/upload/2023/01/16/EDITOR_202301160251204480_i6IVA"
            
            webLinkUrl1 = "https://www.qplace.kr/portfolio/1135"
            webLinkUrl2 = "http://www.zip1004.com/interior/?idx=863088&bmode=view"
            webLinkUrl3 = "https://interior.realestate.daum.net/asp/story/View.do?lnb=2&mngIdx=1722&category=BBS_TY05_AT01_000008&pageIndex=3"
        
        else:
            simpleText = "죄송합니다. 다시 입력해주세요"
            
            
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL1
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl1
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL2
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl2
                                        }
                                    ]
                                },
                                {
                                    "title": title,
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL3
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl3
                                        }
                                    ]
                                },
                                {
                                    "title": "네?",
                                    "description": simpleText,
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": ""
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        print(request.get_json())
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

#-----------------------------------------------------------------------------------[병원]-----------------------------------------------------------------------------------

@app.route('/api/hospital', methods=['POST'])
def hospital():
    try:
        use = request.json.get('action', {}).get('detailParams', {}).get('용도형식', {}).get('value', '')
        
        if(use=="병원"):
            
            title = "여러가지 병원의"
            description = title + " 인테리어입니다"
            imageURL1 = "https://www.dailydental.co.kr/data/photos/20220414/art_164915725959_5bbc07.jpg"
            imageURL2 = "https://cf.zipdoc.co.kr/static/item/40782/20181120120457280_FyRm7OYjM7.jpg"
            imageURL3 = "http://www.designtwoply.com/wp-content/uploads/2020/05/designtwoply0000-1.jpg"
            imageURL4 = "https://www.qplace.kr/data/portfolio/838/d9ea57aa84c3de4d5d3ca66eed35b6de_w800.jpg"
            imageURL5 = "https://www.qplace.kr/data/portfolio/2396/d3cdad42446b13d9bc420c1d04f496d9_w800.jpg"
            imageURL6 = "https://www.qplace.kr/data/portfolio/1913/9c5985c1cc31ce5939e4ab8bfa1462e0_w800.jpg"
            imageURL7 = "https://www.qplace.kr/data/portfolio/1557/62c7d5e6a8ac54cb6942e6e6a59ceb00_w800.jpg"
            imageURL8 = "https://www.qplace.kr/data/portfolio/2227/0b0a246e3d84a608cdbf6af334b32b39_w800.jpg"
            imageURL9 = "https://www.qplace.kr/data/portfolio/1105/a72e39770360e76cede5f32ce04d5619_w800.jpg"
            
            webLinkUrl1 = "https://www.dailydental.co.kr/news/article.html?no=119226"
            webLinkUrl2 = "https://zipdoc.co.kr/product/detail/index/page?category_cd=20&pid=2029"
            webLinkUrl3 = "http://www.designtwoply.com/works/%EC%B2%AD%EC%B6%98%EB%82%B4%EA%B3%BC-%EC%9E%90%EC%97%B0%EC%9D%84-%EB%8B%B4%EC%9D%80-%EB%B3%91%EC%9B%90%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4/"
            webLinkUrl4 = "https://www.qplace.kr/portfolio/838"
            webLinkUrl5 = "https://www.qplace.kr/portfolio/2396"
            webLinkUrl6 = "https://www.qplace.kr/portfolio/1913"
            webLinkUrl7 = "https://www.qplace.kr/portfolio/1557"
            webLinkUrl8 = "https://www.qplace.kr/portfolio/2227"
            webLinkUrl9 = "https://www.qplace.kr/portfolio/1105"
        
        else:
            simpleText = "죄송합니다. 다시 입력해주세요"
            
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "치과",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL1
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl1
                                        }
                                    ]
                                },
                                {
                                    "title": "안과",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL2
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl2
                                        }
                                    ]
                                },
                                {
                                    "title": "내과",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL3
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl3
                                        }
                                    ]
                                },
                                {
                                    "title": "약국",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL4
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl4
                                        }
                                    ]
                                },
                                {
                                    "title": "피부과",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL5
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl5
                                        }
                                    ]
                                },
                                {
                                    "title": "한의원",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL6
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl6
                                        }
                                    ]
                                },
                                {
                                    "title": "정형외과",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL7
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl7
                                        }
                                    ]
                                },
                                {
                                    "title": "성형외과",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL8
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl8
                                        }
                                    ]
                                },
                                {
                                    "title": "산부인과",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL9
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl9
                                        }
                                    ]
                                },
                                {
                                    "title": "네?",
                                    "description": simpleText,
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": ""
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        print(request.get_json())
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

#-----------------------------------------------------------------------------------[주거시설]-----------------------------------------------------------------------------------

@app.route('/api/living', methods=['POST'])
def living():
    try:
        use = request.json.get('action', {}).get('detailParams', {}).get('용도형식', {}).get('value', '')
        
        if(use=="주거시설"):
            
            title = "여러가지 주거시설의"
            description = title + " 인테리어입니다"
            imageURL1 = "https://ms-housing.kr/data/file/residence_gallery/3717996142_JleLZf7s_39d3e5cc7b20b6312ee18ebddd3066f627f8142b.jpg"
            imageURL2 = "https://ms-housing.kr/data/file/residence_gallery/3068357811_xzvNwhTL_a1fcdff0de220b15ad0eb83ec104f3d5527816a6.jpg"
            imageURL3 = "https://ms-housing.kr/data/file/commercial_gallery/3076758371_gZbjwoBl_e5ffa3ce4d0bceebbec43a62193dd014eeb976e6.jpg"
            imageURL4 = "https://postfiles.pstatic.net/MjAyMDA2MTNfMjc0/MDAxNTkyMDMyNjM3MTE2.c6a7helkMCHMD-u4oZ2VK9hFnmPpyVtqncbRIa-ejTQg.v9ygkHMft1_afAlOQ7d4ycH2FDbvcqe4I3YugrRStywg.JPEG.richism7/%EF%BB%BF5%ED%8F%89_%EC%98%A4%ED%94%BC%EC%8A%A4%ED%85%94_%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4_by_%EC%A7%91%EA%BE%B8%EB%AF%B8%EA%B8%B0.jpg?type=w773"
            
            webLinkUrl1 = "https://ms-housing.kr/bbs/board.php?bo_table=residence_gallery&wr_id=832&sop=and&device=pc"
            webLinkUrl2 = "https://ms-housing.kr/bbs/board.php?bo_table=residence_gallery&wr_id=1303&device=pc"
            webLinkUrl3 = "https://ms-housing.kr/bbs/board.php?bo_table=commercial_gallery&wr_id=775"
            webLinkUrl4 = "https://blog.naver.com/PostView.nhn?blogId=richism7&logNo=221999524736"
        
        else:
            simpleText = "죄송합니다. 다시 입력해주세요"
            
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "빌라",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL1
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl1
                                        }
                                    ]
                                },
                                {
                                    "title": "주택",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL2
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl2
                                        }
                                    ]
                                },
                                {
                                    "title": "고시원",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL3
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl3
                                        }
                                    ]
                                },
                                {
                                    "title": "오피스텔",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL4
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl4
                                        }
                                    ]
                                },
                                {
                                    "title": "네?",
                                    "description": simpleText,
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": ""
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        print(request.get_json())
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500
    
#-----------------------------------------------------------------------------------[주거시설(방)]-----------------------------------------------------------------------------------

@app.route('/api/room', methods=['POST'])
def room():
    try:
        use = request.json.get('action', {}).get('detailParams', {}).get('용도형식', {}).get('value', '')
        
        if(use=="주거시설(방)"):
            
            title = "여러가지 방들의"
            description = title + " 인테리어입니다"
            imageURL1 = "https://image.ohou.se/i/bucketplace-v2-development/uploads/cards/snapshots/169173786078345444.jpeg?w=720"
            imageURL2 = "http://www.designtwoply.com/wp-content/uploads/2021/03/designtwoply0000-1.jpg"
            imageURL3 = "https://image.ohou.se/i/bucketplace-v2-development/uploads/cards/snapshots/169087905318351049.jpeg?w=720"
            imageURL4 = "https://www.zipdeco.co.kr/upload/2018/09/10/EDITOR_201809100328054510_u4WFM"
            imageURL5 = "https://image.ohou.se/i/bucketplace-v2-development/uploads/cards/snapshots/168839197074353597.jpeg?w=720"
            
            webLinkUrl1 = "https://contents.ohou.se/cards/26361068?affect_type=CardSearch&affect_id=0&query=%EC%95%88%EB%B0%A9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4"
            webLinkUrl2 = "http://www.designtwoply.com/tag/%EC%A3%BC%EB%B0%A9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4/"
            webLinkUrl3 = "https://contents.ohou.se/cards/26198716?affect_type=CardSearch&affect_id=0&query=%EA%B1%B0%EC%8B%A4%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4"
            webLinkUrl4 = "https://www.zipdeco.co.kr/hs/story/View.do?mngIdx=1274&onstatus="
            webLinkUrl5 = "https://contents.ohou.se/cards/25765410?affect_type=CardSearch&affect_id=0&query=%ED%99%94%EC%9E%A5%EC%8B%A4%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4"
        
        else:
            simpleText = "죄송합니다. 다시 입력해주세요"
            
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "안방",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL1
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl1
                                        }
                                    ]
                                },
                                {
                                    "title": "주방",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL2
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl2
                                        }
                                    ]
                                },
                                {
                                    "title": "거실",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL3
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl3
                                        }
                                    ]
                                },
                                {
                                    "title": "침실",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL4
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl4
                                        }
                                    ]
                                },
                                {
                                    "title": "욕실",
                                    "description": description,
                                    "thumbnail": {
                                        "imageUrl": imageURL5
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": webLinkUrl5
                                        }
                                    ]
                                },
                                {
                                    "title": "네?",
                                    "description": simpleText,
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "링크로 이동",
                                            "webLinkUrl": ""
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        print(request.get_json())
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5032, debug=True)