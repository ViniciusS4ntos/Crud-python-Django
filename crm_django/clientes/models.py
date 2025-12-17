from django.db import models

# O Django usa o ORM para mapear classes para tabelas.
# Como estamos usando 'mysql.connector' diretamente, esta classe é apenas
# para fins de representação e para evitar erros comuns de "AppRegistryNotReady".
class Cliente(models.Model):
    # O seu banco de dados já define o ID, Nome, Email, Telefone.
    # Não vamos usá-lo para fazer o CRUD, mas ele define a estrutura.
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        # Define que o Django não deve gerenciar esta tabela (usaremos a sua)
        # Atenção: Isso é necessário para evitar conflitos se você usar 'manage.py migrate'
        # e é uma prática avançada, mas simplifica o reuso do seu código 'conexao.py'.
        managed = False 
        db_table = 'clientes' # Nome da sua tabela