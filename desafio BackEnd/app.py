from flask import Flask, jsonify, request
from database import create_tables
import task_controller
app = Flask(__name__)

#nomeia como GET através do repositorio aplicacoes
@app.route('/aplicacoes', methods=["GET"])
def get_tasks():
    #tenta a consulta e cria o arquivo Json, retorno 200 para ok
    try:
        tasks = task_controller.get_tasks()
        return jsonify({"tarefas": tasks})
    #em caso de erro, iremos repassar o 400 como padrão
    except Exception as e:
        return jsonify({"message": "Erro ao pegar tarefas"}), 400

#nomeia como POST através do repositorio aplicacoes
@app.route("/aplicacoes", methods=["POST"])
def insert_game():
    #tenta a inserção da nova task no banco
    try:
        game_details = request.get_json()
        name = game_details.get("name")
        description = game_details.get("description")
        result = task_controller.insert_task(name, description)
        #retorna json de tarefa ok
        return jsonify({"message": "Tarefa inserida."})

    #em caso de erro, retorna padrão 400
    except Exception as e:
        return jsonify({"message": "Não foi possível inserir a tarefa."}), 400

if __name__ == "__main__":
    #cria a tabela
    create_tables()
    #permite que o usuário acesse por qualquer IP, pela porta 500
    app.run(host='0.0.0.0', port=5000, debug=False)