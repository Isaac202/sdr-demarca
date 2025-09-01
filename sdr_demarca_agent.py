from dataclasses import dataclass
from typing import Optional
from agents import Agent, function_tool, ModelSettings, Runner
from agents.extensions.memory.sqlalchemy_session import SQLAlchemySession
from datetime import datetime


@dataclass
class UserContext:
    telefone: str
    nome_usuario: Optional[str] = None  # Opcional para futuras melhorias


@function_tool
def enviar_analise_de_marca(nome_marca: str, descricao_negocio: str, telefone: str) -> str:
    """Envia uma solicitação de análise de viabilidade de marca nominativa.

    Args:
        nome_marca: Nome da marca composto somente por letras, números e palavras.  Não inclua logotipos ou elementos figurativos.
        descricao_negocio: Descrição objetiva dos produtos ou serviços e como sua empresa atua.
        telefone: Número de telefone do usuário, usado para associar o relatório.

    Returns:
        Mensagem de confirmação informando que a análise foi solicitada e o prazo de entrega do relatório (ex.: "Seu relatório ficará pronto em até 3 minutos").
    """
    ...


@function_tool
def verificar_relatorio_marca(telefone: str) -> str:
    """Verifica se o relatório de análise de marca está pronto.

    Args:
        telefone: Número de telefone do usuário registrado no sistema.

    Returns:
        Texto contendo a análise gerada (campo `gpt_analysis` do relatório) e, se houver, um `payment_url` para que o cliente realize o pagamento.
    """
    ...


def instrucoes_dinamicas(context: UserContext, agent: Agent[UserContext]) -> str:
    data_atual = datetime.now().strftime("%d/%m/%Y")
    telefone = context.telefone
    return (
        "Você é um SDR da demarca.ai, especializado em marcas nominativas. "
        "Seu papel é educar e conduzir o cliente no processo de análise e registro de marca no INPI. "
        "Use linguagem acessível, amigável e sem juridiquês. Hoje é " + data_atual + ".\n"
        "Fluxo de atendimento:\n"
        "1. Abertura e educação: cumprimente o cliente e explique o objetivo do atendimento. Pergunte se pode seguir com a análise nominativa.\n"
        "2. Coleta: solicite o nome da marca (apenas texto) e a descrição do negócio. Informe que o telefone registrado é " + telefone + ".\n"
        "3. Análise: após coletar as informações, chame a ferramenta enviar_analise_de_marca. Informe que o relatório ficará pronto em até 3 minutos.\n"
        "4. Verificação: use verificar_relatorio_marca com o telefone para obter o relatório. Se houver payment_url, compartilhe o link.\n"
        "5. Pagamento: explique que após a confirmação do pagamento a equipe jurídica iniciará o registro.\n"
        "Regras de conduta: diferencie mensagens do sistema das mensagens do cliente; não peça logotipo ou elementos figurativos; incentive perguntas e esclareça dúvidas antes de avançar."
    )


def get_sdr_demarca_agent(user_id: str) -> Agent[UserContext]:
    # Ajusta eventuais prefixos no número de telefone
    telefone = user_id[2:] if user_id and len(user_id) > 12 else user_id

    return Agent[
        UserContext
    ](
        name="SDR Demarca",
        instructions=instrucoes_dinamicas,
        model="gpt-4o",  # modelo de sua escolha
        tools=[enviar_analise_de_marca, verificar_relatorio_marca],
        model_settings=ModelSettings(tool_choice="required"),  # força o uso das ferramentas
    )


async def atender_cliente() -> None:
    agente = get_sdr_demarca_agent(user_id="5599999999999")
    session = SQLAlchemySession.from_url(
        "session_5599999999999",
        url="postgresql+asyncpg://user:pass@host/dbname",
        create_tables=True,
    )
    contexto = UserContext(telefone="5599999999999")
    resultado = await Runner.run(
        agente,
        "Olá, gostaria de registrar minha marca",
        session=session,
        context=contexto,
    )
    print(resultado.final_output)
