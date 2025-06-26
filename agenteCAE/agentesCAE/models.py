from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator

class AgenteCAE(models.Model):
    # Campos OBRIGATÓRIOS
    SIAPE_agente = models.CharField(
        max_length=7,unique=True,verbose_name="Matrícula do Agente",validators=[MinLengthValidator(5),RegexValidator(r'^\d+$', 'Apenas números são permitidos.')])
    
    cpf_agente = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF do Agente",
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(11),
            RegexValidator(r'^\d+$', 'Apenas números são permitidos.')
        ]
    )
    
    nome_agente = models.CharField(max_length=100, verbose_name="Nome do Agente")
    data_nascimento_agente = models.DateField(verbose_name="Data de Nascimento")
    status_agente = models.BooleanField(default=True, verbose_name="Ativo?")

    # Campos OPCIONAIS
    rg_agente = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="RG do Agente",
        validators=[RegexValidator(r'^\d+$', 'Apenas números são permitidos.')]
    )
    
    email_agente = models.EmailField(blank=True, null=True, verbose_name="E-mail do Agente")
    cargo_agente = models.CharField(max_length=50, blank=True, null=True, verbose_name="Cargo")

    def __str__(self):
        return self.nome_agente

    class Meta:
        verbose_name = "Agente CAE"
        verbose_name_plural = "Agentes CAE"