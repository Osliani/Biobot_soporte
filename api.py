from flask import Flask, request
from openai import OpenAI
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
from datetime import datetime
from waitress import serve
import mongo, tools, utils, os, re

load_dotenv()

def crear_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    openai_client = OpenAI(api_key=OPENAI_API_KEY)

    @app.route('/whatsapp', methods=['POST'])
    def whatsapp_reply():
        incoming_msg = request.form['Body'].strip()
        user_number = re.sub(r'^whatsapp:\+', '', request.values.get('From', ''))
        
        if not incoming_msg:
            return utils.not_message()
        
        conversation = mongo.get_conversation(user_number)
        if not conversation:
            conversation = utils.create_conversation()
        
        conversation.append({
            "role": "user", 
            "content": incoming_msg + "(Fecha: {})".format(datetime.now().strftime('%Y-%m-%d')), 
            "date": datetime.now().strftime('%Y-%m-%d')
        })
        mongo.update_conversation(user_number, conversation)

        print("Mensaje Recibido!")
        print(f"-User: {incoming_msg}")
        
        available_tools = tools.user_tools
        available_functions = tools.user_available_functions
            
        response = utils.generate_response(openai_client, conversation, available_tools)
        tool_calls = response.choices[0].message.tool_calls
        
        if tool_calls:
            print("Tool calls")
            conversation_ext = utils.tools_call(response, conversation, available_functions, user_number)
            if not conversation_ext:
                # clean_chat
                return str(MessagingResponse())
            
            response = utils.generate_response(openai_client, conversation_ext, available_tools)
            ans = response.choices[0].message.content
            
            return utils.reply_text(ans, conversation, user_number)
        
        else:
            ans = response.choices[0].message.content
            return utils.reply_text(ans, conversation, user_number)
            
    return app

if __name__ == '__main__':
    app = crear_app()
    #app.run(debug=True, host='0.0.0.0', port=3024)
    print("API serve on port: 3025")
    serve(app, host='0.0.0.0', port=3025)