# Реестр документов

## Назначение

Реестр содержит уникальные идентификаторы документов,
используемые для связи документов с тестовыми вопросами,
результатами поиска и ответами системы.

## Правила идентификации

- Каждый документ получает уникальный идентификатор.
- Формат идентификатора: DOC001, DOC002 и далее.
- Документы группируются по подразделениям.
- После присвоения ID не изменяется.
- При добавлении документа используется следующий свободный ID.
- ID удалённых документов повторно не используются.

## Структура реестра

| ID     | Имя файла                                               | Название документа                               | Подразделение  | Уровень доступа |
| ------ | ------------------------------------------------------- | ------------------------------------------------ | -------------- | --------------- |
| DOC001 | grafik_obucheniya_personala.docx                        | График обучения персонала                        | HR             | department      |
| DOC002 | instrukciya_po_obnovleniyu_personalnyh_dannyh.docx      | Инструкция по обновлению персональных данных     | HR             | all             |
| DOC003 | instrukciya_po_podgotovke_spravok_sotrudnikam.docx      | Инструкция по подготовке справок сотрудникам     | HR             | all             |
| DOC004 | instrukciya_po_uchetu_rabochego_vremeni.docx            | Инструкция по учёту рабочего времени             | HR             | all             |
| DOC005 | instrukciya_po_vedeniyu_lichnyh_del.docx                | Инструкция по ведению личных дел                 | HR             | department      |
| DOC006 | poryadok_adaptacii_novyh_sotrudnikov.docx               | Порядок адаптации новых сотрудников              | HR             | department      |
| DOC007 | poryadok_naznacheniya_nastavnika.docx                   | Порядок назначения наставника                    | HR             | department      |
| DOC008 | poryadok_oformleniya_trudovogo_dogovora.docx            | Порядок оформления трудового договора            | HR             | department      |
| DOC009 | poryadok_perevoda_mezhdu_podrazdeleniyami.docx          | Порядок перевода между подразделениями           | HR             | all             |
| DOC010 | poryadok_raboty_s_obrashcheniyami_personala.docx        | Порядок работы с обращениями персонала           | HR             | department      |
| DOC011 | poryadok_soglasovaniya_grafikov_otpuskov.docx           | Порядок согласования графиков отпусков           | HR             | department      |
| DOC012 | poryadok_uvolneniya_po_iniciative_sotrudnika.docx       | Порядок увольнения по инициативе сотрудника      | HR             | department      |
| DOC013 | pravila_hraneniya_kadrovykh_dokumentov.pdf              | Правила хранения кадровых документов             | HR             | department      |
| DOC014 | pravila_ispolzovaniya_korporativnoy_formy.pdf           | Правила использования корпоративной формы        | HR             | all             |
| DOC015 | pravila_oformleniya_komandirovki_sotrudnika.pdf         | Правила оформления командировки сотрудника       | HR             | all             |
| DOC016 | pravila_predostavleniya_uchebnogo_otpuska.pdf           | Правила предоставления учебного отпуска          | HR             | all             |
| DOC017 | pravila_udalyonnoy_raboty.pdf                           | Правила удалённой работы                         | HR             | all             |
| DOC018 | reglament_hraneniya_trudovyh_dogovorov.pdf              | Регламент хранения трудовых договоров            | HR             | department      |
| DOC019 | reglament_ocenki_ispytatelnogo_sroka.pdf                | Регламент оценки испытательного срока            | HR             | department      |
| DOC020 | reglament_otpuskov.pdf                                  | Порядок оформления ежегодного отпуска            | HR             | all             |
| DOC021 | reglament_priema_na_rabotu.pdf                          | Регламент приёма на работу                       | HR             | department      |
| DOC022 | reglament_provedeniya_sobesedovaniy.pdf                 | Регламент проведения собеседований               | HR             | department      |
| DOC023 | reglament_vnutrennego_obucheniya.pdf                    | Регламент внутреннего обучения                   | HR             | department      |
| DOC024 | standart_provedeniya_vyhodnogo_intervyu.pdf             | Стандарт проведения выходного интервью           | HR             | department      |
| DOC025 | standart_vvedeniya_novogo_rabotnika_v_dolzhnost.pdf     | Стандарт введения нового работника в должность   | HR             | department      |
| DOC026 | byudzhetirovanie_podrazdeleniy.docx                     | Бюджетирование подразделений                     | Finance        | department      |
| DOC027 | instrukciya_po_kontrolyu_budzetnyh_ostatkov.docx        | Инструкция по контролю бюджетных остатков        | Finance        | department      |
| DOC028 | instrukciya_po_oformleniyu_avansovogo_otcheta.docx      | Инструкция по оформлению авансового отчёта       | Finance        | all             |
| DOC029 | instrukciya_po_oformleniyu_schetov_faktur.docx          | Инструкция по оформлению счетов-фактур           | Finance        | department      |
| DOC030 | instrukciya_po_rabote_s_aktami.docx                     | Инструкция по работе с актами                    | Finance        | department      |
| DOC031 | instrukciya_po_uchetu_osnovnyh_sredstv.docx             | Инструкция по учёту основных средств             | Finance        | department      |
| DOC032 | poryadok_oformleniya_pervichnyh_dokumentov.docx         | Порядок оформления первичных документов          | Finance        | department      |
| DOC033 | poryadok_oplaty_postavshchikam.docx                     | Порядок оплаты поставщикам                       | Finance        | department      |
| DOC034 | poryadok_podgotovki_finansovoy_otchetnosti.docx         | Порядок подготовки финансовой отчётности         | Finance        | department      |
| DOC035 | poryadok_sverki_vzaimoraschetov.docx                    | Порядок сверки взаиморасчётов                    | Finance        | department      |
| DOC036 | poryadok_vozmeshcheniya_komandirovochnyh_rashodov.docx  | Порядок возмещения командировочных расходов      | Finance        | all             |
| DOC037 | poryadok_vozvrata_denezhnyh_sredstv.docx                | Порядок возврата денежных средств                | Finance        | department      |
| DOC038 | poryadok_zakrytiya_otchetnogo_perioda.docx              | Порядок закрытия отчётного периода               | Finance        | department      |
| DOC039 | pravila_arhivacii_finansovyh_dokumentov.docx            | Правила архивации финансовых документов          | Finance        | department      |
| DOC040 | pravila_formirovaniya_platezhnogo_kalendarya.docx       | Правила формирования платёжного календаря        | Finance        | department      |
| DOC041 | pravila_proverki_kontragentov_dlya_oplaty.pdf           | Правила проверки контрагентов для оплаты         | Finance        | department      |
| DOC042 | pravila_raboty_s_podotchetnymi_summami.pdf              | Правила работы с подотчётными суммами            | Finance        | department      |
| DOC043 | pravila_ucheta_predstavitelskih_rashodov.pdf            | Правила учёта представительских расходов         | Finance        | all             |
| DOC044 | reglament_finansovogo_planirovaniya.pdf                 | Регламент финансового планирования               | Finance        | department      |
| DOC045 | reglament_priema_i_proverki_schetov.pdf                 | Регламент приёма и проверки счетов               | Finance        | department      |
| DOC046 | reglament_raboty_s_kassovymi_dokumentami.pdf            | Регламент работы с кассовыми документами         | Finance        | department      |
| DOC047 | reglament_soglasovaniya_biudzheta_proekta.pdf           | Регламент согласования бюджета проекта           | Finance        | department      |
| DOC048 | reglament_soglasovaniya_schetov.pdf                     | Регламент согласования счетов                    | Finance        | department      |
| DOC049 | reglament_ucheta_rashodov_na_svyaz.pdf                  | Регламент учёта расходов на связь                | Finance        | department      |
| DOC050 | instrukciya_po_bezopasnomu_udalennomu_dostupu.docx      | Инструкция по безопасному удалённому доступу     | IT             | all             |
| DOC051 | instrukciya_po_informacionnoy_bezopasnosti.docx         | Инструкция по информационной безопасности        | IT             | all             |
| DOC052 | instrukciya_po_sbrosu_parolya.docx                      | Инструкция по сбросу пароля                      | IT             | all             |
| DOC053 | instrukciya_po_soobshcheniyu_o_fishinge.docx            | Инструкция по сообщению о фишинге                | IT             | all             |
| DOC054 | instrukciya_po_zashchite_rabochego_mesta.docx           | Инструкция по защите рабочего места              | IT             | all             |
| DOC055 | instrukciya_po_zayavkam_v_it.docx                       | Инструкция по оформлению заявок в IT             | IT             | department      |
| DOC056 | poryadok_deystviy_pri_sboye_sistemy.docx                | Порядок действий при сбое системы                | IT             | all             |
| DOC057 | poryadok_podklyucheniya_k_vpn.docx                      | Порядок подключения к VPN                        | IT             | department      |
| DOC058 | poryadok_sozdaniya_rezervnyh_kopiy.docx                 | Порядок создания резервных копий                 | IT             | department      |
| DOC059 | poryadok_uvedomleniya_o_tehnicheskih_rabotah.docx       | Порядок уведомления о технических работах        | IT             | all             |
| DOC060 | poryadok_vosstanovleniya_dannyh.docx                    | Порядок восстановления данных                    | IT             | all             |
| DOC061 | poryadok_zakrytiya_dostupa_uvolennogo.docx              | Порядок закрытия доступа уволенного сотрудника   | IT             | department      |
| DOC062 | pravila_hraneniya_rezervnyh_kopiy.pdf                   | Правила хранения резервных копий                 | IT             | department      |
| DOC063 | pravila_ispolzovaniya_korporativnoy_pochty.pdf          | Правила использования корпоративной почты        | IT             | all             |
| DOC064 | pravila_ispolzovaniya_oblachnyh_servisov.pdf            | Правила использования облачных сервисов          | IT             | all             |
| DOC065 | pravila_ispolzovaniya_vneshnih_nositeley.pdf            | Правила использования внешних носителей          | IT             | all             |
| DOC066 | pravila_naznacheniya_prav_dostupa.pdf                   | Правила назначения прав доступа                  | IT             | department      |
| DOC067 | reglament_obnovleniya_programmnogo_obespecheniya.pdf    | Регламент обновления программного обеспечения    | IT             | department      |
| DOC068 | reglament_reakcii_na_informacionnyy_incident.pdf        | Регламент реакции на информационный инцидент     | IT             | department      |
| DOC069 | reglament_sozdaniya_uchetnyh_zapisey.pdf                | Регламент создания учётных записей               | IT             | department      |
| DOC070 | reglament_testirovaniya_rezervnogo_vosstanovleniya.pdf  | Регламент тестирования резервного восстановления | IT             | department      |
| DOC071 | reglament_upravleniya_kompyuternym_oborudovaniem.pdf    | Регламент управления компьютерным оборудованием  | IT             | department      |
| DOC072 | reglament_zakupki_oborudovaniya.pdf                     | Регламент закупки оборудования                   | IT             | department      |
| DOC073 | standart_inventarizacii_it_aktivov.pdf                  | Стандарт инвентаризации IT-активов               | IT             | department      |
| DOC074 | standart_priema_it_obrashcheniy.pdf                     | Стандарт приёма IT-обращений                     | IT             | department      |
| DOC075 | instrukciya_po_formirovaniyu_voronki_prodazh.docx       | Инструкция по формированию воронки продаж        | Sales          | department      |
| DOC076 | instrukciya_po_podgotovke_otcheta_o_prodazhah.docx      | Инструкция по подготовке отчёта о продажах       | Sales          | department      |
| DOC077 | instrukciya_po_rabote_s_poteryannymi_sdelkami.docx      | Инструкция по работе с потерянными сделками      | Sales          | department      |
| DOC078 | instrukciya_po_vedeniyu_klientskoy_bazy.docx            | Инструкция по ведению клиентской базы            | Sales          | department      |
| DOC079 | poryadok_podgotovki_dogovornogo_predlozheniya.docx      | Порядок подготовки договорного предложения       | Sales          | department      |
| DOC080 | poryadok_provedeniya_analiza_potrebnostey.docx          | Порядок проведения анализа потребностей          | Sales          | department      |
| DOC081 | poryadok_raboty_s_obrashcheniyami_klientov.docx         | Порядок работы с обращениями клиентов            | Sales          | department      |
| DOC082 | poryadok_raboty_s_reklamaciyami_klientov.docx           | Порядок работы с рекламациями клиентов           | Sales          | department      |
| DOC083 | poryadok_uchyota_vstrech_s_klientami.docx               | Порядок учёта встреч с клиентами                 | Sales          | department      |
| DOC084 | pravila_hraneniya_perepiski_s_klientami.pdf             | Правила хранения переписки с клиентами           | Sales          | department      |
| DOC085 | pravila_podgotovki_kommercheskogo_raschyota.pdf         | Правила подготовки коммерческого расчёта         | Sales          | department      |
| DOC086 | pravila_podgotovki_kommercheskih_prezentaciy.pdf        | Правила подготовки коммерческих презентаций      | Sales          | department      |
| DOC087 | pravila_soglasovaniya_skidok.pdf                        | Правила согласования скидок                      | Sales          | department      |
| DOC088 | reglament_kvalifikacii_potencialnogo_klienta.pdf        | Регламент квалификации потенциального клиента    | Sales          | department      |
| DOC089 | reglament_peredachi_klienta_mezhdu_menedzherami.pdf     | Регламент передачи клиента между менеджерами     | Sales          | department      |
| DOC090 | reglament_provedeniya_demonstracii_produkta.pdf         | Регламент проведения демонстрации продукта       | Sales          | department      |
| DOC091 | reglament_soglasovaniya_usloviy_postavki.pdf            | Регламент согласования условий поставки          | Sales          | department      |
| DOC092 | standart_obsluzhivaniya_klientov.pdf                    | Стандарт обслуживания клиентов                   | Sales          | department      |
| DOC093 | standart_otveta_na_vhodyashchiy_zapros.pdf              | Стандарт ответа на входящий запрос               | Sales          | department      |
| DOC094 | standart_podgotovki_kommercheskogo_predlozheniya.pdf    | Стандарт подготовки коммерческого предложения    | Sales          | department      |
| DOC095 | standart_soprovozhdeniya_klienta_posle_prodazhi.pdf     | Стандарт сопровождения клиента после продажи     | Sales          | department      |
| DOC096 | standart_telefonnyh_peregovorov.pdf                     | Стандарт телефонных переговоров                  | Sales          | department      |
| DOC097 | standart_vzaimodeystviya_s_novym_klientom.pdf           | Стандарт взаимодействия с новым клиентом         | Sales          | department      |
| DOC098 | poryadok_rassmotreniya_sluzhebnyh_zaprosov.docx         | Порядок рассмотрения служебных запросов          | Administrative | all             |
| DOC099 | pravila_bronirovaniya_peregovornyh.docx                 | Правила бронирования переговорных                | Administrative | all             |
| DOC100 | pravila_organizacii_korporativnyh_meropriyatiy.pdf      | Правила организации корпоративных мероприятий    | HR             | all             |
| DOC101 | poryadok_predostavleniya_administrativnogo_dostupa.docx | Порядок предоставления административного доступа | IT             | admin           |
