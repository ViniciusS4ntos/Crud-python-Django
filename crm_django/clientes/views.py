from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .cadastrar import cadastrar_cliente # Reutilizando sua função
from .conexao import conectar
import re

# Esta função de utilidade recupera um cliente por ID (reutilizado de main.py)
def _obter_cliente_por_id(id_cliente):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email, telefone FROM clientes WHERE id = %s", (id_cliente,))
        cliente_data = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if cliente_data:
            # Retorna um dicionário para fácil uso no template
            return {
                'id': cliente_data[0],
                'nome': cliente_data[1],
                'email': cliente_data[2],
                'telefone': cliente_data[3]
            }
    return None

# 1. VISUALIZAR CLIENTES (Lista)
def listar_clientes(request):
    conn = conectar()
    clientes = []
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email, telefone FROM clientes ORDER BY nome")
        resultados = cursor.fetchall()

        # Transforma a tupla em uma lista de dicionários para o template
        for cliente in resultados:
            clientes.append({
                'id': cliente[0], 
                'nome': cliente[1], 
                'email': cliente[2], 
                'telefone': cliente[3]
            })
        
        cursor.close()
        conn.close()

    # Renderiza o template de lista e passa os clientes
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

# 2. CADASTRAR CLIENTE (Formulário e Envio)
def cadastrar_cliente_web(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        
        # Chama sua função original de cadastrar
        # Nota: Sua função 'cadastrar_cliente' imprime a mensagem de sucesso/erro.
        # Em um projeto Django real, você usaria o sistema de "messages".
        cadastrar_cliente(nome, email, telefone) 
        
        # Redireciona para a lista após o cadastro
        return redirect('listar_clientes')

    # Se não for POST (é GET), mostra o formulário
    return render(request, 'clientes/cadastrar_cliente.html')

# 3. EDITAR CLIENTE (Formulário e Envio)
def editar_cliente_web(request, id):
    cliente = _obter_cliente_por_id(id)

    if not cliente:
        # Em um projeto real, você retornaria uma página 404
        return HttpResponse("Cliente não encontrado!", status=404)

    if request.method == 'POST':
        # Adaptação da sua lógica de editar_cliente do main.py
        novo_nome = request.POST.get('nome').strip()
        novo_email = request.POST.get('email').strip()
        novo_telefone = request.POST.get('telefone').strip()
        
        # Lógica para manter o valor atual se o campo estiver vazio
        nome_final = novo_nome.title() if novo_nome else cliente['nome']
        email_final = novo_email.lower() if novo_email else cliente['email']
        telefone_final = novo_telefone if novo_telefone else cliente['telefone']
        
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE clientes
                SET nome = %s, email = %s, telefone = %s
                WHERE id = %s
            """, (nome_final, email_final, telefone_final, id))
            conn.commit()
            cursor.close()
            conn.close()
            
            # Redireciona para a lista após a edição
            return redirect('listar_clientes')

    # Se não for POST (é GET), mostra o formulário com dados atuais
    return render(request, 'clientes/editar_cliente.html', {'cliente': cliente})

# 4. REMOVER CLIENTE (Confirmação e Remoção)
def remover_cliente_web(request, id):
    cliente = _obter_cliente_por_id(id)

    if not cliente:
        return HttpResponse("Cliente não encontrado!", status=404)

    if request.method == 'POST':
        # Remove o cliente
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
            conn.commit()
            cursor.close()
            conn.close()
        
        # Redireciona para a lista
        return redirect('listar_clientes')

    # Se for GET, mostra a página de confirmação
    return render(request, 'clientes/remover_cliente.html', {'cliente': cliente})