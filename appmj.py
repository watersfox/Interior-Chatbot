# 1. 스킬서버예제(1)
from flask import Flask, request, jsonify
import sys
#1

app = Flask(__name__)

@app.route('/api/sayHello', methods=['GET'])
def hello():
    return "Hello Kakao-Chatbot!!"

# 1) 카카오톡 텍스트형 응답
@app.route('/api/sayHello', methods=['POST'])
def seyHello():
    user_message = request.json.get('userRequest', {}).get('utterance', '')
    #print(body)
    user_message=int(user_message)

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": user_message + 100000
                    }
                }
            ]
        }
    }
    
    return responseBody;

# 2) 카카오톡 이미지형 응답
@app.route('/api/showHello', methods=['POST'])
def showHello():
    body = request.get_json()
    # print(body)
    
    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                        "altText": "hello I'm Kakao.Chatbot!!"
                    } 
                }
            ]
        }
    }
    
    return responseBody;

@app.route('/api/showHello5', methods=['POST'])
def showHello5():
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
                                },
                                {
                                    "title": "This is another Title",
                                    "description": "This is another description.",
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
                                },
                                {
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
    
@app.route('/api/showCard', methods=['POST'])
def showCard():
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
                                },
                                {
                                    "title": "This is another Title",
                                    "description": "This is another description.",
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
                                },
                                {
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
    app.run(host='0.0.0.0', port=)  # web server