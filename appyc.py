from flask import Flask, request, jsonify
import re
import pymysql
import json
#http://ec2-13-125-206-239.ap-northeast-2.compute.amazonaws.com:5000

app = Flask(__name__)





# get방식
@app.route('/api/sayHello', methods=['GET'])
def hello():
    return "Hello Kakao-Chatbot!!"

# 카드형 응답
@app.route('/api/showHello', methods=['POST'])
def showHello():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": "This is a Title",
                            "description": "This is a description.",
                            "thumbnail": {
                                "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg"
                            },
                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": "링크로 이동",
                                    "webLinkUrl": "https://www.naver.com"
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

#입력메시지 출력
@app.route('/api/usertext', methods=['POST'])
def sayHello2():
    try:
        # 카카오톡에서 받은 사용자의 입력 메시지
        user_message = request.json.get('userRequest', {}).get('utterance', '')

        # 응답 구성
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": f"사용자가 입력한 메시지: {user_message}"
                        }
                    }
                ]
            }
        }

        return responseBody
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

# 게시판링크
@app.route('/menuLink', methods=['POST'])
def menuLink():
    try:
        title = request.json.get('action', {}).get('detailParams', {}).get('게시판메뉴', {}).get('value', '')
        
        if title == "고객후기":
            webLinkUrl = "https://zipdoc.co.kr/postscript?category_cd=90"
        
        elif title == "시공사례":
            webLinkUrl = "https://zipdoc.co.kr/product/construction/list"
        
        elif title == "인테리어 팁":
            webLinkUrl = "https://zipdoc.co.kr/story/list?magazineType=1#page%3D1"
        
        elif title == "인테리어 아이디어":
            webLinkUrl = "https://zipdoc.co.kr/product/resident/items"
        
        elif (title == "고객상담") or (title == ""):
            title = "고객상담"
            webLinkUrl = "https://zipdoc.co.kr/customer/faq"

        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                {
                    "textCard": {
                    "title": title,
                    "description": title+" 게시판으로 이동하는 링크입니다.",
                    "buttons": [
                        {
                        "action": "webLink",
                        "label": title+" 게시판으로 이동",
                        "webLinkUrl": webLinkUrl
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

# 인테리어업체 지도 링크
@app.route('/mapLink', methods=['POST'])
def mapLink():
    try:
        loc = request.json.get('action', {}).get('detailParams', {}).get('지역', {}).get('origin', '')

        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "textCard": {
                            "title": loc+" 인테리어 업체",
                            "description": loc+" 주변 인테리어 업체를 검색합니다.",
                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": "이동",
                                    "webLinkUrl": "https://www.google.com/maps/search/"+loc+"+인테리어/data=!3m1!4b1?entry=ttu"
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
    app.run(host='0.0.0.0', port=5031)