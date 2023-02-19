import datetime
import pandas as pd
import pandas_market_calendars as mcal


cod_vencimento = {"F": 1, "G": 2, "H": 3, "J": 4, "K": 5, "M": 6, "N": 7, "Q": 8, "U": 9, "V": 10, "X": 11, "Z": 12}

def DOL_WDO_DI1(ticker: str) -> datetime.date:
    """
    Último dia de negociação: Sessão de negociação anterior à data de vencimento.

    Data de vencimento: 1º dia útil do mês de vencimento.

    Meses de vencimento: Todos os meses.
    """

    # Extrair informação do symbol (Código do Ativo, Més de Vencimento, Ano de Vencimento)
    reference_month_code: str = ticker[3]
    reference_month: int = int(cod_vencimento[reference_month_code])
    reference_year: int = int('20' + ticker[-2:])

    if reference_month == 1:
        # Nesse caso, olhar o calendário do mẽs anterior ao mês de referencia
        start_date: str = str(datetime.datetime(reference_year - 1, 12, 1))
        end_date: str = str(datetime.datetime(reference_year - 1, 12, 31))

        # calendário de dias úteis da B3
        b3_calendar = mcal.get_calendar('BVMF')
        early = b3_calendar.schedule(start_date=start_date, end_date=end_date)

        # dias úteis para o mês de referência
        wdays: pd.DataFrame = pd.DataFrame(early.index, columns=['date'])
    else:
        start_date: str = str(datetime.datetime(reference_year, reference_month - 1, 1))
        end_date: str = str(datetime.datetime(reference_year, reference_month, 1))

        # calendário de dias úteis da B3
        b3_calendar = mcal.get_calendar('BVMF')
        early = b3_calendar.schedule(start_date=start_date, end_date=end_date)

        # dias úteis para o mês de referência (filtra o prmeiro dia do mês seguinte)
        wdays: pd.DataFrame = pd.DataFrame(early.index, columns=['date'])
        wdays = wdays.loc[wdays['date'].dt.month == reference_month - 1]

    # Retorna o último dia útil do mês anterior ao de vencimento
    return pd.to_datetime(wdays.tail(1).values[0][0]).date()

def expiration_WIN(ticker: str) -> datetime.date:
    """
    Último dia de negociação: Quarta-feira mais próxima do dia 15 do mês de vencimento.

    Data de vencimento: Quarta-feira mais próxima do dia 15 do mês de vencimento.
    Caso não houver sessão de negociação, a data de vencimento será a próxima sessão de negociação.

    Meses de vencimento: Meses pares.
    """

    # Extrair informação do symbol (Código do Ativo, Més de Vencimento, Ano de Vencimento)
    reference_month_code: str = ticker[3]
    reference_month: int = int(cod_vencimento[reference_month_code])
    reference_year: int = int('20' + ticker[-2:])

    # Nesse caso, olhar o calendário do mẽs anterior ao mês de Vencimento
    start_date: str = str(datetime.datetime(reference_year, reference_month, 1))

    if reference_month == 12:
        end_date: str = str(datetime.datetime(reference_year, reference_month, 31))
    else:
        end_date: str = str(datetime.datetime(reference_year, reference_month + 1, 1))

    # calendário de dias úteis da B3
    b3_calendar = mcal.get_calendar('BVMF')
    early = b3_calendar.schedule(start_date=start_date, end_date=end_date)

    # dias úteis para o mês de referência (filtra o prmeiro dia do mês seguinte)
    wdays: pd.DataFrame = pd.DataFrame(early.index, columns=['date'])
    wdays = wdays.loc[wdays['date'].dt.month == reference_month]

    reference_date = datetime.datetime(reference_year, reference_month, 15)
    past_counter = 0
    past_days = wdays[
        wdays['date'] < reference_date
    ]['date'].map(datetime.datetime.date).values.tolist()[::-1]

    future_counter = 0
    future_days = wdays[
        wdays['date'] > reference_date
    ]['date'].map(datetime.datetime.date).values.tolist()

    if pd.to_datetime(reference_date) in wdays['date'].values and reference_date.weekday() == 2:
        return str(reference_date.date())
    else:
        while True:
            p = past_days[past_counter]

            if p.weekday() == 2:
                break
            else:
                past_counter += 1

        while True:
            f = future_days[future_counter]

            if f.weekday() == 2:
                break
            else:
                future_counter += 1

        if past_counter >= future_counter:
            return future_days[future_counter]
        else:
            return past_days[past_counter]


def expiration_IND(ticker: str) -> datetime.date:
    """
    Último dia de negociação: Quarta-feira mais próxima do dia 15 do mês de vencimento.

    Data de vencimento: Quarta-feira mais próxima do dia 15 do mês de vencimento.
    Caso não houver sessão de negociação, a data de vencimento será a próxima sessão de negociação.

    Meses de vencimento: Meses pares.
    """

    # Extrair informação do symbol (Código do Ativo, Més de Vencimento, Ano de Vencimento)
    reference_month_code: str = ticker[3]
    reference_month: int = int(cod_vencimento[reference_month_code])
    reference_year: int = int('20' + ticker[-2:])

    # Nesse caso, olhar o calendário do mẽs anterior ao mês de Vencimento
    start_date: str = str(datetime.datetime(reference_year, reference_month, 1))

    if reference_month == 12:
        end_date: str = str(datetime.datetime(reference_year, reference_month, 31))
    else:
        end_date: str = str(datetime.datetime(reference_year, reference_month + 1, 1))

    # calendário de dias úteis da B3
    b3_calendar = mcal.get_calendar('BVMF')
    early = b3_calendar.schedule(start_date=start_date, end_date=end_date)

    # dias úteis para o mês de referência (filtra o prmeiro dia do mês seguinte)
    wdays: pd.DataFrame = pd.DataFrame(early.index, columns=['date'])
    wdays = wdays.loc[wdays['date'].dt.month == reference_month]

    reference_date = datetime.datetime(reference_year, reference_month, 15)
    past_counter = 0
    past_days = wdays[
        wdays['date'] < reference_date
    ]['date'].map(datetime.datetime.date).values.tolist()[::-1]

    future_counter = 0
    future_days = wdays[
        wdays['date'] > reference_date
    ]['date'].map(datetime.datetime.date).values.tolist()

    if pd.to_datetime(reference_date) in wdays['date'].values and reference_date.weekday() == 2:
        return str(reference_date.date())
    else:
        while True:
            p = past_days[past_counter]

            if p.weekday() == 2:
                break
            else:
                past_counter += 1

        while True:
            f = future_days[future_counter]

            if f.weekday() == 2:
                break
            else:
                future_counter += 1

        if past_counter >= future_counter:
            return future_days[future_counter]
        else:
            return past_days[past_counter]


def expiration_BGI_ETN(ticker: str) -> datetime.date:
    """
    Último dia de negociação: Última sessão de negociação do mês de vencimento do contrato.

    Data de vencimento:	Última sessão de negociação do mês de vencimento do contrato.

    Meses de vencimento: Todos os meses.
    """

    # Extrair informação do symbol (Código do Ativo, Més de Vencimento, Ano de Vencimento)
    reference_month_code: str = ticker[3]
    reference_month: int = int(cod_vencimento[reference_month_code])
    reference_year: int = int('20' + ticker[-2:])

    # Caso o mês de vencimento seja dezembro, olhar o calendário do mês de dezembro
    if reference_month == 12:
        # Data de inicio e fim do calendário do mês de referência
        start_date: str = str(datetime.datetime(reference_year, reference_month, 1))
        end_date: str = str(datetime.datetime(reference_year, 12, 31))
        # calendário de dias úteis da B3
        b3_calendar = mcal.get_calendar('BVMF')
        early = b3_calendar.schedule(start_date=start_date, end_date=end_date)
        # coluna dos dias de abertura
        wdays: pd.DataFrame = pd.DataFrame(early.index, columns=['date'])
    else:
        # Nesse caso, olhar o calendário do mês anterior ao mês de Vencimento
        start_date: str = str(datetime.datetime(reference_year, reference_month, 1))
        reference_month = reference_month + 1
        end_date: str = str(datetime.datetime(reference_year, reference_month, 1))

        # calendário de dias úteis da B3
        b3_calendar = mcal.get_calendar('BVMF')
        early = b3_calendar.schedule(start_date=start_date, end_date=end_date)

        # coluna dos dias de abertura
        wdays: pd.DataFrame = pd.DataFrame(early.index, columns=['date'])
        wdays = wdays.loc[wdays['date'].dt.month == reference_month - 1]

    # Retorna o último dia útil do mês de vencimento
    return pd.to_datetime(wdays.tail(1).values[0][0]).date()


def expiration_SFI(ticker: str) -> datetime.date:
    """
    Último dia de negociação: 2º dia útil anterior ao mês de vencimento.

    Data de vencimento: 2º dia útil anterior ao mês de vencimento.

    Meses de vencimento: Março, abril, maio, junho, julho, agosto, setembro e novembro.
    """

    # Extrair informação do symbol (Código do Ativo, Més de Vencimento, Ano de Vencimento)
    reference_month_code: str = ticker[3]
    reference_month: int = int(cod_vencimento[reference_month_code])

    reference_year: int = int('20' + ticker[-2:])

    # Nesse caso, olhar o calendário do mẽs anterior ao mês de Vencimento
    start_date: str = str(datetime.datetime(reference_year, reference_month - 1, 1))
    end_date: str = str(datetime.datetime(reference_year, reference_month, 1))

    # calendário de dias úteis da B3
    b3_calendar = mcal.get_calendar('BVMF')
    early = b3_calendar.schedule(start_date=start_date, end_date=end_date)

    # coluna dos dias de abertura
    wdays: pd.DataFrame = pd.DataFrame(early.index, columns=['date'])
    wdays = wdays.loc[wdays['date'].dt.month == reference_month - 1]

    # Retorna o penúltimo dia útil do mês anterior ao mês de vencimento do contrato de SFI
    return pd.to_datetime(wdays.tail(2).values[0][0]).date()


def expiration_CCM(ticker: str) -> datetime.date:
    """
    Último dia de negociação: Dia 15 do mês de vencimento.

    Data de vencimento:	Dia 15 do mês de vencimento. Caso não haja sessão de negociação, a data de
    vencimento será a próxima sessão de negociação.

    Meses de vencimento: Janeiro, março, maio, julho, agosto, setembro e novembro.
    """

    # Extrair informação do symbol (Código do Ativo, Més de Vencimento, Ano de Vencimento)
    reference_month_code: str = ticker[3]
    reference_month: int = int(cod_vencimento[reference_month_code])
    reference_year: int = int('20' + ticker[-2:])

    # Nesse caso, olhar o calendário do mẽs anterior ao mês de Vencimento
    start_date: str = str(datetime.datetime(reference_year, reference_month, 1))
    end_date: str = str(datetime.datetime(reference_year, reference_month + 1, 1))

    # calendário de dias úteis da B3
    b3_calendar = mcal.get_calendar('BVMF')
    early = b3_calendar.schedule(start_date=start_date, end_date=end_date)

    # coluna dos dias de abertura
    wdays: pd.Series = early['market_close'].dt.strftime('%Y-%m-%d')
    wdays: pd.DataFrame = wdays.to_frame()
    wdays.columns = ['date']

    reference_month = str(reference_month)
    reference_year = str(reference_year)

    # Retorna o dia 15 do mês de vencimento,
    # caso não haja dia 15, retorna o proximo dia ultil
    day_expiration = wdays[
        reference_year + '-' + reference_month + '-' + '15':
    ].head(1).values[0][0]

    # convert do datetime.date object
    day_expiration = datetime.datetime.strptime(day_expiration, '%Y-%m-%d').date()

    return day_expiration


def expiration_ICF(ticker: str) -> datetime.date:
    """
    Último dia de negociação: 6º dia útil anterior ao último dia útil do mês do vencimento.

    Data de vencimento:	6º dia útil anterior ao último dia útil do mês do vencimento.
    Caso não haja sessão de negociação, a data de vencimento será a próxima sessão de negociação.

    Meses de vencimento: Março, maio, julho, setembro e dezembro.
    """

    reference_month_code: str = ticker[3]
    reference_month: int = int(cod_vencimento[reference_month_code])
    reference_year: int = int('20' + ticker[-2:])

    # Nesse caso, olhar o calendário do mẽs anterior ao mês de Vencimento
    start_date: str = str(datetime.datetime(reference_year, reference_month, 1))
    if reference_month == 12 or reference_month == 9:
        if reference_month == 12:
            reference_month = 0
            reference_year += 1
        # var é a quantidade de dias que o calendario vai para trás
        var = 7
    else:
        var = 8
    end_date: str = str(datetime.datetime(reference_year, reference_month + 1, 1))

    # calendário de dias úteis da B3
    b3_calendar = mcal.get_calendar('BVMF')
    early = b3_calendar.schedule(start_date=start_date, end_date=end_date)

    # coluna dos dias de abertura
    wdays: pd.Series = early['market_close'].dt.strftime('%Y-%m-%d')
    wdays: pd.DataFrame = wdays.to_frame()
    wdays.columns = ['date']

    reference_month = str(reference_month)
    reference_year = str(reference_year)

    # Retorna o sexto dia util anterior ao ultimo dia util do mes de vencimento
    return pd.to_datetime(wdays.tail(var).values[0][0]).date()

