
from fastapi import FastAPI

app = FastAPI()


questions = [

    {
        "tid": "24480000-5d64-0015-d47a-08d8dfd78d10",
        "taskContent": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>W celu utrwalenia barwy mięsa i nadania mu specyficznego smaku, stosuje się</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>solenie.</p>",
                "answerId": "24650000-5d64-0015-cf36-08d8dfd78e7a",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>wędzenie.</p>",
                "answerId": "24650000-5d64-0015-4994-08d8dfd78e7b",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>peklowanie.</p>",
                "answerId": "24650000-5d64-0015-8d71-08d8dfd78e7b",
                "Correct": True
            },
            {
                "answerKey": 8,
                "answerText": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>pasteryzację.</p>",
                "answerId": "24650000-5d64-0015-e0cd-08d8dfd78e7b",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-6d79-08d8dfd7c5b8",
        "taskContent": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>Ile koncentratu jabłkowego potrzeba do sporządzenia 20 l napoju jabłkowo-miętowego, jeżeli do wyprodukowania 100 l gotowego produktu zużywa się 5,5 kg koncentratu?</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>1,10 kg</p>",
                "answerId": "24650000-5d64-0015-4eaa-08d8dfd7c722",
                "Correct": True
            },
            {
                "answerKey": 2,
                "answerText": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>2,75 kg</p>",
                "answerId": "24650000-5d64-0015-e31a-08d8dfd7c722",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>5,50 kg</p>",
                "answerId": "24650000-5d64-0015-2ba9-08d8dfd7c723",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>11,0 kg</p>",
                "answerId": "24650000-5d64-0015-7019-08d8dfd7c723",
                "Correct": False
            }
        ]
    },

    {
        "tid": "24480000-5d64-0015-36a8-08d8dfd97ad4",
        "taskContent": "<p>W gospodarstwie ekologicznym do nawożenia mineralnego można zastosować</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>siarczan potasu.</p>",
                "answerId": "24650000-5d64-0015-45e9-08d8dfd97c47",
                "Correct": True
            },
            {
                "answerKey": 2,
                "answerText": "<p>wapno tlenkowe.</p>",
                "answerId": "24650000-5d64-0015-aba0-08d8dfd97c47",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>saletrę amonową.</p>",
                "answerId": "24650000-5d64-0015-05c1-08d8dfd97c48",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>superfosfat potrójny granulowany.</p>",
                "answerId": "24650000-5d64-0015-49fb-08d8dfd97c48",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-8ad0-08d8dfd9e15d",
        "taskContent": "<p>Na zdjęciu widoczna jest</p><p style=\"text-align: right;\"><img style=\"width:329px;height:226px;\" src=\"/Content/Media/24480000-5d64-0015-44e6-08d8dfda2045.JPG\" alt=\"\" width=\"329\" height=\"226\" data-sizetype=\"px\" data-mce-src=\"../../../filemanager/connectors/TaskProductionTaskFile/filemanager.TaskProductionTaskFile?mode=preview&amp;path=24480000-5d64-0015-44e6-08d8dfda2045\" data-mce-style=\"width: 329px; height: 226px;\"></p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>cynia.</p>",
                "answerId": "24650000-5d64-0015-10c5-08d8dfd9e2ca",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>rudbekia.</p>",
                "answerId": "24650000-5d64-0015-d1fe-08d8dfd9e2cb",
                "Correct": True
            },
            {
                "answerKey": 4,
                "answerText": "<p>nasturcja.</p>",
                "answerId": "24650000-5d64-0015-1a9f-08d8dfd9e2cd",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>aksamitka.</p>",
                "answerId": "24650000-5d64-0015-94c6-08d8dfd9e2cd",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-3d62-08d8dfda5753",
        "taskContent": "<p style=\"text-align: center;\"><img style=\"width:530px;height:174px;\" src=\"/Content/Media/24480000-5d64-0015-6257-08d8dfda7c21.JPG\" alt=\"\" width=\"530\" height=\"174\" data-sizetype=\"px\" data-mce-src=\"../../../filemanager/connectors/TaskProductionTaskFile/filemanager.TaskProductionTaskFile?mode=preview&amp;path=24480000-5d64-0015-6257-08d8dfda7c21\" data-mce-style=\"width: 530px; height: 174px;\"><br></p><p style=\"text-align: left;\">Nasiona bratka ogrodowego wysiewa się</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>latem do gruntu.</p>",
                "answerId": "24650000-5d64-0015-7117-08d8dfda58bc",
                "Correct": True
            },
            {
                "answerKey": 2,
                "answerText": "<p>zimą do szklarni.</p>",
                "answerId": "24650000-5d64-0015-f902-08d8dfda58bc",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>późną wiosną do gruntu.</p>",
                "answerId": "24650000-5d64-0015-3e73-08d8dfda58bd",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>wczesną wiosną do gruntu.</p>",
                "answerId": "24650000-5d64-0015-8361-08d8dfda58bd",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-5b07-08d8dfdabc0f",
        "taskContent": "<p>Strzałką oznaczono element pługa. Jest to</p><p style=\"text-align: right;\"><img style=\"width:300px;height:210px;\" src=\"/Content/Media/24480000-5d64-0015-33d3-08d8dfdad7c1.JPG\" alt=\"\" width=\"300\" height=\"210\" data-sizetype=\"px\" data-mce-src=\"../../../filemanager/connectors/TaskProductionTaskFile/filemanager.TaskProductionTaskFile?mode=preview&amp;path=24480000-5d64-0015-33d3-08d8dfdad7c1\" data-mce-style=\"width: 300px; height: 210px;\"></p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>odkładnica.</p>",
                "answerId": "24650000-5d64-0015-3d11-08d8dfdabd7a",
                "Correct": True
            },
            {
                "answerKey": 2,
                "answerText": "<p>lemiesz.</p>",
                "answerId": "24650000-5d64-0015-c0ae-08d8dfdabd7a",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>piętka.</p>",
                "answerId": "24650000-5d64-0015-3e53-08d8dfdabd7b",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>płoza.</p>",
                "answerId": "24650000-5d64-0015-85b6-08d8dfdabd7b",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-e3fb-08d8dfdb7d12",
        "taskContent": "<p>Na podstawie opisu wyglądu zewnętrznego wskaż ten, który przedstawia mąkę żytnią razową.</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>Kolor szaro-kremowy, z widocznymi cząsteczkami otrąb.</p>",
                "answerId": "24650000-5d64-0015-a041-08d8dfdb7e89",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>Kolor biały z odcieniem kremowym, bez widocznych otrąb.</p>",
                "answerId": "24650000-5d64-0015-fabb-08d8dfdb7e89",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>Kolor szary, z widocznymi cząsteczkami okrywy owocowo-nasiennej.</p>",
                "answerId": "24650000-5d64-0015-4400-08d8dfdb7e8a",
                "Correct": True
            },
            {
                "answerKey": 8,
                "answerText": "<p>Kolor biały, z odcieniem szarości, bez cząsteczek okrywy owocowo-nasiennej.</p>",
                "answerId": "24650000-5d64-0015-97a3-08d8dfdb7e8a",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-224f-08d8dfdbaab3",
        "taskContent": "<p>Na podstawie atestu mąki pszennej dostarczonej do piekarni wskaż mąkę najlepszej jakości.</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>Wilgotność 14%, zawartość glutenu 28.</p>",
                "answerId": "24650000-5d64-0015-1fc8-08d8dfdbac1d",
                "Correct": True
            },
            {
                "answerKey": 2,
                "answerText": "<p>Wilgotność 14%, zawartość glutenu 23.</p>",
                "answerId": "24650000-5d64-0015-bb51-08d8dfdbac1d",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>Wilgotność 17%, zawartość glutenu 29.</p>",
                "answerId": "24650000-5d64-0015-0872-08d8dfdbac1e",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>Wilgotność 15%, zawartość glutenu 22.</p>",
                "answerId": "24650000-5d64-0015-4d83-08d8dfdbac1e",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-daff-08d8dfdc7972",
        "taskContent": "<p>Wybierz prawidłową temperaturę przechowywania drożdży piekarskich.</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>-18°C</p>",
                "answerId": "24650000-5d64-0015-a527-08d8dfdc7ad9",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>-3°C</p>",
                "answerId": "24650000-5d64-0015-0cd0-08d8dfdc7ada",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>+5°C</p>",
                "answerId": "24650000-5d64-0015-3c11-08d8dfdc7ada",
                "Correct": True
            },
            {
                "answerKey": 8,
                "answerText": "<p>+12°C</p>",
                "answerId": "24650000-5d64-0015-7e22-08d8dfdc7ada",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-2c84-08d8dfdd0938",
        "taskContent": "<p>Do której grupy należy pieczywo, w którym udział margaryny i cukru w cieście wynosi 14%?</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>Pieczywo pszenne półcukiernicze.</p>",
                "answerId": "24650000-5d64-0015-5400-08d8dfdd0aa6",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>Pieczywo pszenne wyborowe.</p>",
                "answerId": "24650000-5d64-0015-fc5a-08d8dfdd0aa7",
                "Correct": True
            },
            {
                "answerKey": 4,
                "answerText": "<p>Pieczywo pszenne zwykłe.</p>",
                "answerId": "24650000-5d64-0015-cf6a-08d8dfdd0aaa",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>Pieczywo pszenno-żytnie.</p>",
                "answerId": "24650000-5d64-0015-5fbf-08d8dfdd0aac",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-bc6f-08d8dfdd4671",
        "taskContent": "<p>Którą metodą należy sporządzić ciasto na rogale wyborowe mając do dyspozycji mąkę pszenną o mocnym glutenie?</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>Na kwasie.</p>",
                "answerId": "24650000-5d64-0015-8291-08d8dfdd47db",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>Dwufazową.</p>",
                "answerId": "24650000-5d64-0015-bb95-08d8dfdd47db",
                "Correct": True
            },
            {
                "answerKey": 4,
                "answerText": "<p>Jednofazową.</p>",
                "answerId": "24650000-5d64-0015-e150-08d8dfdd47db",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>Pięciofazową.</p>",
                "answerId": "24650000-5d64-0015-04d7-08d8dfdd47dc",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-bad7-08d8dfdd9d17",
        "taskContent": "<p>Wybierz zestaw urządzeń służących do formowania chleba zwykłego podłużnego.</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>Dzielarka i rogalikarka.</p>",
                "answerId": "24650000-5d64-0015-06b3-08d8dfdd9e80",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>Dzielarka i bagieciarka.</p>",
                "answerId": "24650000-5d64-0015-7b75-08d8dfdd9e80",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>Zaokrąglarka i wydłużarka.</p>",
                "answerId": "24650000-5d64-0015-b9ba-08d8dfdd9e80",
                "Correct": True
            },
            {
                "answerKey": 8,
                "answerText": "<p>Zaokrąglarka i znakownica.</p>",
                "answerId": "24650000-5d64-0015-f138-08d8dfdd9e80",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-b49d-08d8dfddd033",
        "taskContent": "<p>W jakim celu stosuje się nacinanie kęsów ciasta w czasie rozrostu?</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>Zapobiegania deformacjom oraz w celach dekoracyjnych.</p>",
                "answerId": "24650000-5d64-0015-faee-08d8dfddd19c",
                "Correct": True
            },
            {
                "answerKey": 2,
                "answerText": "<p>Zmniejszenia objętości oraz pozbycia się gazów.</p>",
                "answerId": "24650000-5d64-0015-7ae9-08d8dfddd19d",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>Zwiększenia parowania oraz obsuszania kęsów.</p>",
                "answerId": "24650000-5d64-0015-c3dd-08d8dfddd19d",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>Zwiększenia objętości oraz powstania aromatu.</p>",
                "answerId": "24650000-5d64-0015-0fa7-08d8dfddd19e",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-2b6a-08d8dfde0d9e",
        "taskContent": "<p>Przed wypiekiem uformowane kęsy ciasta na chały zdobne należy</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>zwilżyć wodą i ponakłuwać.</p>",
                "answerId": "24650000-5d64-0015-9635-08d8dfde0f12",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>zwilżyć wodą i ponacinać ukośnie.</p>",
                "answerId": "24650000-5d64-0015-ebb1-08d8dfde0f12",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>posmarować masą jajową i posypać solą.</p>",
                "answerId": "24650000-5d64-0015-42b3-08d8dfde0f13",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>posmarować masą jajową i posypać kruszonką.</p>",
                "answerId": "24650000-5d64-0015-9099-08d8dfde0f13",
                "Correct": True
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-12ab-08d8dfde3e43",
        "taskContent": "<p>Podczas I fazy wypieku w kęsach ciasta następuje</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>utrwalenie kształtu.</p>",
                "answerId": "24650000-5d64-0015-f5af-08d8dfde3fa7",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>ukształtowanie skórki.</p>",
                "answerId": "24650000-5d64-0015-3e76-08d8dfde3fa8",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>zwiększenie objętości.</p>",
                "answerId": "24650000-5d64-0015-735e-08d8dfde3fa8",
                "Correct": True
            },
            {
                "answerKey": 8,
                "answerText": "<p>powstanie związków aromatycznych.</p>",
                "answerId": "24650000-5d64-0015-9d0c-08d8dfde3fa8",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-9c22-08d8dfde7409",
        "taskContent": "<p>Których z przedstawionych metod <span style=\"text-decoration: underline;\"><strong>nie stosuje się</strong></span> w celu sprawdzenia zakończenia wypieku?</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>Opukiwania pieczywa i ważenia.</p>",
                "answerId": "24650000-5d64-0015-8224-08d8dfde7572",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>Nakłuwania szpilą i oceny wzrokowej.</p>",
                "answerId": "24650000-5d64-0015-10fd-08d8dfde7573",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>Oceny wzrokowej i ważenia pieczywa.</p>",
                "answerId": "24650000-5d64-0015-5612-08d8dfde7573",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>Naświetlania promieniami UV i naciskania.</p>",
                "answerId": "24650000-5d64-0015-96cc-08d8dfde7573",
                "Correct": True
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-affc-08d8dfdf4b34",
        "taskContent": "<p>Co może być przyczyną powstawania ciemnych pęcherzy na skórce pieczywa?</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>Nieodpowiednie warunki fermentacji ciasta.</p>",
                "answerId": "24650000-5d64-0015-8eb7-08d8dfdf4ca1",
                "Correct": True
            },
            {
                "answerKey": 2,
                "answerText": "<p>Nadmierna ilość dodanej do ciasta soli.</p>",
                "answerId": "24650000-5d64-0015-0ea2-08d8dfdf4ca3",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>Niska temperatura wypieku.</p>",
                "answerId": "24650000-5d64-0015-85bf-08d8dfdf4ca4",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>Zbyt długi czas wypieku.</p>",
                "answerId": "24650000-5d64-0015-e49b-08d8dfdf4ca5",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-4b09-08d8dfdf9b2d",
        "taskContent": "<p>W magazynie wyrobów gotowych znajduje się 660 sztuk bochenków chleba o gramaturze 0,80 kg oraz 300 sztuk bułek maślanych. Wiedząc, że w jeden pojemnik głęboki można zapakować 6 sztuk chleba, a w płaski 15 sztuk bułek, oblicz ile pojemników każdego rodzaju będzie potrzebnych do zapakowania tej produkcji.</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>Głębokich 115, płaskich 20.</p>",
                "answerId": "24650000-5d64-0015-c488-08d8dfdf9c95",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>Głębokich 100, płaskich 30.</p>",
                "answerId": "24650000-5d64-0015-49ae-08d8dfdf9c96",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>Głębokich 115, płaskich 30.</p>",
                "answerId": "24650000-5d64-0015-8fd2-08d8dfdf9c96",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>Głębokich 110, płaskich 20.</p>",
                "answerId": "24650000-5d64-0015-d813-08d8dfdf9c96",
                "Correct": True
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-d4f0-08d8dfe015a1",
        "taskContent": "<p>Półproduktem cukierniczym jest</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>nadzienie makowe.</p>",
                "answerId": "24650000-5d64-0015-9400-08d8dfe01714",
                "Correct": True
            },
            {
                "answerKey": 2,
                "answerText": "<p>mąka pszenna.</p>",
                "answerId": "24650000-5d64-0015-22a7-08d8dfe01715",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>cukier puder.</p>",
                "answerId": "24650000-5d64-0015-7447-08d8dfe01715",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>jaja świeże.</p>",
                "answerId": "24650000-5d64-0015-c86a-08d8dfe01715",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-eeac-08d8dfe04280",
        "taskContent": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>Mąkę należy przechowywać w temperaturze</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>0°C przy wilgotności powietrza 55%</p>",
                "answerId": "24650000-5d64-0015-1378-08d8dfe043ea",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>14°C przy wilgotności powietrza 65%</p>",
                "answerId": "24650000-5d64-0015-a171-08d8dfe043ea",
                "Correct": True
            },
            {
                "answerKey": 4,
                "answerText": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>18°C przy wilgotności powietrza 75%</p>",
                "answerId": "24650000-5d64-0015-e2ae-08d8dfe043ea",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<div id=\"MathJax_Message\" style=\"display: none;\"></div><p>20°C przy wilgotności powietrza 85%</p>",
                "answerId": "24650000-5d64-0015-1f1f-08d8dfe043eb",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-60ef-08d8dfe06f23",
        "taskContent": "<p>Pomiar wilgotności w magazynie surowców suchych dokonuje się</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>refraktometrem.</p>",
                "answerId": "24650000-5d64-0015-ca5b-08d8dfe0708d",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>termometrem.</p>",
                "answerId": "24650000-5d64-0015-6193-08d8dfe07090",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>higrometrem.</p>",
                "answerId": "24650000-5d64-0015-aca9-08d8dfe07090",
                "Correct": True
            },
            {
                "answerKey": 8,
                "answerText": "<p>areometrem.</p>",
                "answerId": "24650000-5d64-0015-fc18-08d8dfe07090",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-84d8-08d8dfe0b2f8",
        "taskContent": "<p>Sporządzając ciasto biszkoptowo-tłuszczowe metodą na ciepło podgrzewa się</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>masę jajową.</p>",
                "answerId": "24650000-5d64-0015-d8ce-08d8dfe0b461",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>tłuszcz z mąką.</p>",
                "answerId": "24650000-5d64-0015-7ce6-08d8dfe0b462",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>mleko z cukrem.</p>",
                "answerId": "24650000-5d64-0015-c3e3-08d8dfe0b462",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>masę jajowo-cukrową.</p>",
                "answerId": "24650000-5d64-0015-097c-08d8dfe0b463",
                "Correct": True
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-c8c7-08d8dfe0fd5d",
        "taskContent": "<p>Wskaż ilość margaryny niezbędną do wyprodukowania 20 kg ciastek kruchych krakowskich</p><p style=\"text-align: right;\"><img style=\"width:356px;height:201px;\" src=\"/Content/Media/24480000-5d64-0015-e818-08d8dfe1233a.JPG\" alt=\"\" width=\"356\" height=\"201\" data-sizetype=\"px\" data-mce-src=\"../../../filemanager/connectors/TaskProductionTaskFile/filemanager.TaskProductionTaskFile?mode=preview&amp;path=24480000-5d64-0015-e818-08d8dfe1233a\" data-mce-style=\"width: 356px; height: 201px;\"></p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>4,5 kg</p>",
                "answerId": "24650000-5d64-0015-2144-08d8dfe0fec9",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>5,7 kg</p>",
                "answerId": "24650000-5d64-0015-df65-08d8dfe0fec9",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>7,6 kg</p>",
                "answerId": "24650000-5d64-0015-2cca-08d8dfe0feca",
                "Correct": True
            },
            {
                "answerKey": 8,
                "answerText": "<p>8,9 kg</p>",
                "answerId": "24650000-5d64-0015-7727-08d8dfe0feca",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-4b90-08d8dfe1584e",
        "taskContent": "<p>Do ubijania białek z cukrem w ubijaczce cukierniczej stosuje się mieszadło w kształcie</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>ramy.</p>",
                "answerId": "24650000-5d64-0015-5101-08d8dfe159b7",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>haka.</p>",
                "answerId": "24650000-5d64-0015-da3b-08d8dfe159b7",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>rózgi.</p>",
                "answerId": "24650000-5d64-0015-2cd8-08d8dfe159b8",
                "Correct": True
            },
            {
                "answerKey": 8,
                "answerText": "<p>spirali.</p>",
                "answerId": "24650000-5d64-0015-6f8b-08d8dfe159b8",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-8d69-08d8dfe1ccf8",
        "taskContent": "<p>Do dekoracji tortu w stylu angielskim stosuje się</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>marcepan naturalny.</p>",
                "answerId": "24650000-5d64-0015-3c53-08d8dfe1ce64",
                "Correct": True
            },
            {
                "answerKey": 2,
                "answerText": "<p>świeże owoce.</p>",
                "answerId": "24650000-5d64-0015-c43e-08d8dfe1ce64",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>czekoladę.</p>",
                "answerId": "24650000-5d64-0015-69c6-08d8dfe1ce65",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>karmel.</p>",
                "answerId": "24650000-5d64-0015-f589-08d8dfe1ce65",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-e344-08d8dfe1faa2",
        "taskContent": "<p>Pomadki mleczne „Krówki” zawija się w</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>papier parafinowany.</p>",
                "answerId": "24650000-5d64-0015-962d-08d8dfe1fc16",
                "Correct": True
            },
            {
                "answerKey": 2,
                "answerText": "<p>torebki celofanowe.</p>",
                "answerId": "24650000-5d64-0015-feb2-08d8dfe1fc16",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>folię aluminiową.</p>",
                "answerId": "24650000-5d64-0015-5f77-08d8dfe1fc17",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>papier kredowy.</p>",
                "answerId": "24650000-5d64-0015-b8de-08d8dfe1fc17",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-c065-08d8dfe23e2c",
        "taskContent": "<p>Wskaż urządzenie, w którym należy przechowywać lody.</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>Lada chłodnicza.</p>",
                "answerId": "24650000-5d64-0015-05ea-08d8dfe23f93",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>Lada mroźnicza.</p>",
                "answerId": "24650000-5d64-0015-7a4e-08d8dfe23f93",
                "Correct": True
            },
            {
                "answerKey": 4,
                "answerText": "<p>Szafa chłodnicza.</p>",
                "answerId": "24650000-5d64-0015-c4dd-08d8dfe23f93",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>Komora chłodnicza.</p>",
                "answerId": "24650000-5d64-0015-1110-08d8dfe23f94",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-34e4-08d8dfe2d117",
        "taskContent": "<p>Do wykonania dekoracji stołu w formie wieńca z żywych kwiatów jest najodpowiedniejsza</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>obręcz ze słomy.</p>",
                "answerId": "24650000-5d64-0015-298e-08d8dfe2d281",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>obręcz ze styropianu.</p>",
                "answerId": "24650000-5d64-0015-c8d4-08d8dfe2d281",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>baza z gąbką florystyczną.</p>",
                "answerId": "24650000-5d64-0015-1e39-08d8dfe2d282",
                "Correct": True
            },
            {
                "answerKey": 8,
                "answerText": "<p>baza z tworzywa sztucznego.</p>",
                "answerId": "24650000-5d64-0015-66dd-08d8dfe2d282",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-4f61-08d8dfe31649",
        "taskContent": "<p>Pojemnik do dekoracji słonecznego tarasu w stylu meksykańskim zostanie obsadzony</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>azaliami.</p>",
                "answerId": "24650000-5d64-0015-9aae-08d8dfe317b2",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>paprociami.</p>",
                "answerId": "24650000-5d64-0015-1879-08d8dfe317b4",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>storczykami.</p>",
                "answerId": "24650000-5d64-0015-89e8-08d8dfe317b4",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>sukulentami.</p>",
                "answerId": "24650000-5d64-0015-d46d-08d8dfe317b4",
                "Correct": True
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-4298-08d8dfe3457c",
        "taskContent": "<p>W kaskadowym bukiecie ślubnym wymagającym wyginania roślin pod dużym kątem stosuje się technikę</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>szynowania.</p>",
                "answerId": "24650000-5d64-0015-1dd3-08d8dfe346e6",
                "Correct": True
            },
            {
                "answerKey": 2,
                "answerText": "<p>splatania.</p>",
                "answerId": "24650000-5d64-0015-bb9c-08d8dfe346e6",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>owijania.</p>",
                "answerId": "24650000-5d64-0015-47b7-08d8dfe346e7",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>klejenia.</p>",
                "answerId": "24650000-5d64-0015-b571-08d8dfe346e7",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-6ba5-08d8dfe3cad9",
        "taskContent": "<p>Do bukietu, w którym zgodnie z trendami mają dominować barwy ciepłe, należy wykorzystać kwiaty o barwie</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>żółtej, pomarańczowej i czerwonej.</p>",
                "answerId": "24650000-5d64-0015-7cae-08d8dfe3cc43",
                "Correct": True
            },
            {
                "answerKey": 2,
                "answerText": "<p>czerwonej, fioletowej i niebieskiej.</p>",
                "answerId": "24650000-5d64-0015-2738-08d8dfe3cc44",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>zielonej, żółtej i pomarańczowej.</p>",
                "answerId": "24650000-5d64-0015-8d28-08d8dfe3cc44",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>żółtej, pomarańczowej i białej.</p>",
                "answerId": "24650000-5d64-0015-dc01-08d8dfe3cc44",
                "Correct": False
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-6c7f-08d8dfe40eb5",
        "taskContent": "<p>Trwałość kwiatów ciętych obniża obecność etylenu w powietrzu. Jego źródłem mogą być</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>rośliny w zbyt wczesnym stadium zbiorczym.</p>",
                "answerId": "24650000-5d64-0015-06bd-08d8dfe4101e",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>rośliny o intensywnie pachnących kwiatach.</p>",
                "answerId": "24650000-5d64-0015-9ceb-08d8dfe4101e",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>rośliny o liściach pokrytych włoskami.</p>",
                "answerId": "24650000-5d64-0015-e9ef-08d8dfe4101e",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>przekwitające kwiaty cięte i owoce.</p>",
                "answerId": "24650000-5d64-0015-4779-08d8dfe4101f",
                "Correct": True
            }
        ]
    },
    {
        "tid": "24480000-5d64-0015-dfe5-08d8dfe44cf8",
        "taskContent": "<p>Ozdobę ślubną w formie kuli z goździków w czasie transportu zabezpiecza się</p>",
        "answer": [
            {
                "answerKey": 1,
                "answerText": "<p>zawijając w mokre płótno.</p>",
                "answerId": "24650000-5d64-0015-25d0-08d8dfe44e64",
                "Correct": False
            },
            {
                "answerKey": 2,
                "answerText": "<p>owijając ciasno celofanem.</p>",
                "answerId": "24650000-5d64-0015-af72-08d8dfe44e64",
                "Correct": False
            },
            {
                "answerKey": 4,
                "answerText": "<p>pakując w biały papier pakowy.</p>",
                "answerId": "24d650000-5d64-0015-fdb6-08d8dfe44e64",
                "Correct": False
            },
            {
                "answerKey": 8,
                "answerText": "<p>pakując w karton wyłożony miękkim papierem.</p>",
                "answerId": "24650000-5d64-0015-4335-08d8dfe44e65",
                "Correct": True
            }
        ]
    }
]





@app.get("/")

def read_root():
    return {"Hello":"World"}


@app.get("/questions")
def get_questions():
    return {"questions":questions}
