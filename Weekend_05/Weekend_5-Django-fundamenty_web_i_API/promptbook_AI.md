# 🤖 Weekend 5 — Promptbook AI: Django, DRF, debugowanie i testy API

> **Kurs:** AI Python Engineer  
> **Blok:** Weekend 5 — Django: fundamenty web i API  
> **Typ pliku:** promptbook do pracy z AI  
> **Cel:** używać AI jako asystenta do nauki, debugowania, testowania i porządkowania projektu — bez bezmyślnego kopiowania gotowców

---

## 🧭 Jak korzystać z tego promptbooka?

Ten plik zawiera gotowe prompty do pracy z AI podczas Weekendu 5.

Używaj AI jako asystenta do:

- wyjaśniania błędów,
- porządkowania myślenia,
- generowania przypadków testowych,
- sprawdzania struktury projektu,
- tworzenia przykładów requestów JSON,
- review kodu,
- przygotowania krótkiej dokumentacji API,
- ćwiczenia rozmowy technicznej.

Nie używaj AI do wygenerowania całego projektu za jednym razem.

Celem tego weekendu jest zrozumienie kodu, który później samodzielnie utrzymasz i rozwiniesz w capstone.

---

## Spis treści

- [Jak korzystać z tego promptbooka?](#-jak-korzystać-z-tego-promptbooka)
- [Zasada pracy z AI w tym bloku](#-zasada-pracy-z-ai-w-tym-bloku)
- [Szybka mapa promptów](#-szybka-mapa-promptów)
- [Debugowanie Django](#-debugowanie-django)
- [Request-response i struktura projektu](#-request-response-i-struktura-projektu)
- [Serializery i walidacja DRF](#-serializery-i-walidacja-drf)
- [APIView, ViewSet i routery](#-apiview-viewset-i-routery)
- [Requesty JSON i statusy HTTP](#-requesty-json-i-statusy-http)
- [Testy API](#-testy-api)
- [Dokumentacja API](#-dokumentacja-api)
- [Capstone](#-capstone)
- [Nauka i rozmowa techniczna](#-nauka-i-rozmowa-techniczna)
- [Antyprompty — czego unikać](#-antyprompty--czego-unikać)
- [Mini-checklista użycia AI](#-mini-checklista-użycia-ai)
- [Najważniejsza zasada](#-najważniejsza-zasada)

---

# ✅ Zasada pracy z AI w tym bloku

Dobry prompt powinien zawierać:

1. **Kontekst** — co budujesz.
2. **Fragment kodu albo komunikat błędu** — zanonimizowany, bez sekretów.
3. **Konkretne pytanie** — co AI ma sprawdzić lub wyjaśnić.
4. **Ograniczenie poziomu** — np. „wyjaśnij jak początkującemu”.
5. **Prośbę o kroki diagnostyczne** — nie od razu pełne rozwiązanie.
6. **Zakaz generowania całego projektu** — szczególnie przy debugowaniu.

---

## Dobry styl promptu

```text
Buduję pierwsze API w Django REST Framework. Jestem początkujący.
Wyjaśnij mi błąd prostym językiem i wskaż 3 rzeczy do sprawdzenia.
Nie generuj całego projektu od nowa.
```

---

## Najważniejsza zasada bezpieczeństwa

Nie wklejaj do AI:

- haseł,
- tokenów,
- sekretów,
- plików `.env`,
- danych klientów,
- prywatnych danych użytkowników,
- pełnych poufnych fragmentów firmowego kodu.

Zamiast tego używaj neutralnych przykładów:

```text
Mam token zapisany w zmiennej środowiskowej, ale aplikacja go nie widzi.
Jak sprawdzić, czy Django poprawnie odczytuje zmienną?
```

---

# 🗺️ Szybka mapa promptów

| Kategoria | Kiedy użyć? | Numery promptów |
|---|---|---|
| Debugowanie Django | błędy, 404, importy, tracebacki | 1–3, 27 |
| Request-response | nie rozumiesz przepływu Django | 4 |
| Struktura projektu | chcesz sprawdzić katalogi i pliki | 5–7 |
| Serializery | projektowanie i review walidacji | 8–10 |
| Statusy HTTP | dobór statusów i błędy API | 11 |
| APIView / ViewSet / Router | widoki API i routing DRF | 12–14, 31 |
| Requesty JSON | potrzebujesz payloadów do testów | 15 |
| Testy API | przypadki testowe, GET, POST, walidacja | 16–21 |
| Dokumentacja API | README/API docs | 22–23 |
| Capstone | dobór domeny, encji, endpointów | 24–26 |
| Nauka i rozmowa | powtórka, interview, zadania domowe | 28–30, 32–35 |

---

# 🧯 Debugowanie Django

## 1. Wyjaśnienie błędu Django

Użyj, gdy masz długi traceback i nie wiesz, od czego zacząć.

```text
Buduję projekt Django dla aplikacji tasks. Jestem na etapie routingu i widoków.

Mam taki błąd:

WKLEJ_TUTAJ_TRACEBACK

Wyjaśnij mi:
1. co oznacza ten błąd prostym językiem,
2. w którym pliku prawdopodobnie jest problem,
3. jakie 3 rzeczy powinienem sprawdzić po kolei,
4. czego nie powinienem zmieniać na ślepo.

Nie podawaj pełnego gotowego projektu. Pomóż mi zdebugować istniejący kod.
```

---

## 2. Debugowanie błędu 404

Użyj, gdy endpoint nie działa, a Django pokazuje 404.

```text
W Django wchodzę na adres:

WKLEJ_TUTAJ_ADRES_URL

Dostaję błąd 404.

Moja struktura URL wygląda tak:

config/urls.py:
WKLEJ_TUTAJ_CONFIG_URLS

tasks/urls.py:
WKLEJ_TUTAJ_TASKS_URLS

Wyjaśnij, dlaczego Django może nie widzieć tego adresu.
Podaj checklistę diagnostyczną dla początkującego.
```

---

## 3. Debugowanie błędu importu

Użyj przy `ImportError`, `ModuleNotFoundError`, złej ścieżce importu albo problemach po przeniesieniu aplikacji.

```text
Mam błąd importu w projekcie Django:

WKLEJ_TUTAJ_TRACEBACK

Struktura projektu:

WKLEJ_TUTAJ_STRUKTURE_KATALOGOW

Plik, w którym pojawia się import:

WKLEJ_TUTAJ_FRAGMENT_KODU

Pomóż mi znaleźć przyczynę.
Nie przepisuj całego kodu.
Wyjaśnij, czy problem dotyczy nazwy pliku, nazwy aplikacji, ścieżki importu, czy konfiguracji INSTALLED_APPS.
```

---

## 27. Wyjaśnienie tracebacka bez gotowca

Użyj, gdy chcesz krótką, uporządkowaną diagnozę.

```text
Mam taki traceback:

WKLEJ_TUTAJ_TRACEBACK

Odpowiedz w formacie:

Problem w skrócie:
Prawdopodobny plik:
Prawdopodobna linia:
Co sprawdzić najpierw:
Co sprawdzić potem:
Czego nie robić:
Minimalna poprawka:

Nie generuj całego projektu.
```

---

# 🔁 Request-response i struktura projektu

## 4. Wyjaśnienie przepływu request-response

Użyj, gdy chcesz zrozumieć, co dzieje się w Django krok po kroku.

```text
Wyjaśnij mi na przykładzie Django, co dzieje się krok po kroku, gdy użytkownik wchodzi na adres:

/api/tasks/

W odpowiedzi użyj mojego poziomu: początkujący Python developer.

Uwzględnij:
- config/urls.py,
- tasks/urls.py,
- view,
- serializer,
- Response,
- status HTTP.

Nie używaj zaawansowanych tematów typu middleware, authentication, permissions ani ORM.
```

---

## 5. Review struktury projektu

Użyj, gdy chcesz sprawdzić, czy katalogi i pliki są sensownie ułożone.

```text
Buduję pierwszy backend Django pod projekt końcowy kursu.

Moja struktura projektu wygląda tak:

WKLEJ_TUTAJ_STRUKTURE_KATALOGOW

Oceń, czy ta struktura jest dobra na start. Zwróć uwagę na:
1. czy projekt i aplikacja są dobrze rozdzielone,
2. czy pliki są w dobrych miejscach,
3. czy czegoś brakuje pod API,
4. czy coś może sprawić problem początkującemu.

Odpowiedz praktycznie, bez przesadnego refaktoringu.
```

---

## 6. Wyjaśnienie różnicy: projekt Django vs aplikacja Django

Użyj, gdy mylisz `config/` z aplikacją biznesową.

```text
Wyjaśnij mi różnicę między projektem Django a aplikacją Django na przykładzie backendu do zarządzania zadaniami.

Użyj prostego języka i analogii z realną aplikacją webową.

Na końcu podaj przykład:
- co powinno być w config/,
- co powinno być w tasks/.
```

---

## 7. Pomoc przy `INSTALLED_APPS`

Użyj, gdy Django nie widzi aplikacji albo DRF.

```text
Mam projekt Django i aplikację:

NAZWA_APLIKACJI

Mój fragment INSTALLED_APPS wygląda tak:

WKLEJ_TUTAJ_INSTALLED_APPS

Sprawdź, czy poprawnie dodałem Django REST Framework i aplikację domenową.
Wyjaśnij, co może się stać, jeśli zapomnę dodać aplikację do INSTALLED_APPS.
```

---

# 🧪 Serializery i walidacja DRF

## 8. Pomoc przy serializerze

Użyj, gdy projektujesz serializer od zera.

```text
Buduję serializer DRF dla encji:

NAZWA_ENCJI

Pola biznesowe:

WKLEJ_TUTAJ_LISTE_POL

Chcę użyć zwykłego serializers.Serializer, nie ModelSerializer.

Pomóż mi zaprojektować serializer z:
- polami wymaganymi,
- polami opcjonalnymi,
- ChoiceField dla statusu lub kategorii,
- sensownymi max_length.

Dodaj krótkie wyjaśnienie, dlaczego każde pole ma taki typ.
```

---

## 9. Review serializera

Użyj, gdy masz już serializer i chcesz go sprawdzić.

```text
Oto mój serializer DRF:

WKLEJ_TUTAJ_KOD_SERIALIZERA

Sprawdź:
1. czy pola wymagane są poprawnie ustawione,
2. czy wartości słownikowe powinny być ChoiceField,
3. czy pole description powinno pozwalać na pusty tekst,
4. czy serializer dobrze pasuje do endpointu POST.

Nie zmieniaj stylu całego projektu. Zaproponuj minimalne poprawki.
```

---

## 10. Wyjaśnienie błędów walidacji

Użyj, gdy DRF zwraca `serializer.errors` i chcesz zrozumieć odpowiedź.

```text
Mój endpoint DRF zwraca taki błąd walidacji:

WKLEJ_TUTAJ_RESPONSE_JSON

Wyjaśnij:
1. które pola są błędne,
2. dlaczego DRF zwraca taki format,
3. jaki status HTTP powinien mieć taki błąd,
4. jak frontend może użyć tej odpowiedzi.

Wyjaśnij prostym językiem.
```

---

# 🧩 APIView, ViewSet i routery

## 12. Review widoku APIView

Użyj, gdy masz gotowy widok i chcesz sprawdzić, czy logika GET/POST jest poprawna.

```text
Oto mój widok APIView w Django REST Framework:

WKLEJ_TUTAJ_KOD_WIDOKU

Sprawdź:
1. czy GET zwraca poprawny status,
2. czy POST używa serializera,
3. czy błędne dane zwracają 400,
4. czy poprawne dane zwracają 201,
5. czy kod jest zrozumiały dla początkującego.

Nie przepisuj na ViewSet. Najpierw oceń wersję APIView.
```

---

## 13. Przejście z APIView na ViewSet

Użyj, gdy działający endpoint APIView chcesz przepisać na prosty ViewSet.

```text
Mam działający endpoint APIView:

WKLEJ_TUTAJ_KOD_APIVIEW

Chcę zrozumieć, jak przepisać go na prosty ViewSet.

Pokaż:
1. które części APIView odpowiadają metodom list i create,
2. jak wygląda minimalny ViewSet,
3. jak podłączyć DefaultRouter,
4. jakie endpointy powstaną.

Nie używaj jeszcze ModelViewSet ani modeli Django.
```

---

## 14. Wyjaśnienie routera DRF

Użyj, gdy nie wiesz, co robi `DefaultRouter`.

```text
Wyjaśnij mi, jak działa DefaultRouter w Django REST Framework.

Mam taki kod:

WKLEJ_TUTAJ_KOD_ROUTERA

Wyjaśnij:
1. co robi router.register,
2. po co jest basename,
3. jakie URL-e powstaną,
4. dlaczego przy ViewSet nie piszę ręcznie path dla każdej metody.
```

---

## 31. Prompt do porównania APIView i ViewSet

Użyj przy powtórce albo przed refaktorem.

```text
Porównaj APIView i ViewSet na przykładzie endpointów:

GET /api/tasks/
POST /api/tasks/

Pokaż tabelę:
- co piszę w APIView,
- co piszę w ViewSet,
- jak wygląda routing,
- kiedy wybrać które podejście.

Wyjaśnij to dla osoby początkującej.
```

---

# 📡 Requesty JSON i statusy HTTP

## 11. Dobór statusów HTTP

Użyj, gdy nie wiesz, czy zwrócić `200`, `201`, `400`, `404` lub `500`.

```text
Buduję API w Django REST Framework.

Dopasuj właściwe statusy HTTP do sytuacji:

1. Pobranie listy zadań.
2. Utworzenie nowego zadania.
3. Brak wymaganego pola title.
4. Niepoprawna wartość statusu.
5. Zadanie o podanym id nie istnieje.
6. Nieobsłużony wyjątek w kodzie.

Podaj status, nazwę i krótkie wyjaśnienie.
```

---

## 15. Generowanie przykładowych requestów JSON

Użyj, gdy chcesz ręcznie przetestować endpoint.

```text
Mam endpoint:

POST /api/tasks/

Serializer przyjmuje pola:
- title: string, wymagane,
- description: string, opcjonalne,
- status: todo, in_progress albo done,
- priority: low, medium albo high.

Wygeneruj:
1. jeden poprawny payload JSON,
2. payload bez title,
3. payload z błędnym statusem,
4. payload z błędnym priorytetem,
5. payload minimalny, ale poprawny.

Nie dodawaj pól, których nie ma w serializerze.
```

---

## 33. Prompt do sprawdzenia REST-owego nazewnictwa

Użyj, gdy masz listę endpointów i chcesz sprawdzić, czy są sensowne.

```text
Mam takie endpointy:

WKLEJ_TUTAJ_LISTE_ENDPOINTOW

Sprawdź, czy są zgodne z praktycznym stylem REST.

Zwróć uwagę na:
- rzeczowniki zamiast czasowników,
- metody HTTP,
- liczbę mnogą zasobów,
- spójność URL-i,
- statusy HTTP.

Zaproponuj lepsze nazwy, jeśli trzeba.
```

---

## 34. Prompt do mapowania API na SQL

Użyj przed kolejnym blokiem o bazie danych i ORM.

```text
Mam endpointy:

GET /api/tasks/
POST /api/tasks/
GET /api/tasks/{id}/
PATCH /api/tasks/{id}/
DELETE /api/tasks/{id}/

Wyjaśnij koncepcyjnie, jakie operacje SQL odpowiadają tym endpointom.

Nie pisz jeszcze kodu Django ORM. Pokaż tylko:
- endpoint,
- metoda HTTP,
- operacja SQL,
- typowy status HTTP.
```

---

# 🧪 Testy API

## 16. Generowanie przypadków testowych

Użyj przed pisaniem testów.

```text
Mam endpoint API:

GET /api/tasks/
POST /api/tasks/

Pola:
- title,
- description,
- status,
- priority.

Zaproponuj minimum 8 przypadków testowych dla początkującego backend developera.

Podziel je na:
- happy path,
- walidacja,
- edge cases,
- kontrakt API.

Dla każdego przypadku podaj:
- nazwę testu,
- co testuje,
- oczekiwany status HTTP.
```

---

## 17. Pomoc przy teście GET

Użyj, gdy piszesz pierwszy test endpointu listy.

```text
Chcę napisać test endpointu:

GET /api/tasks/

Używam pytest i APIClient z Django REST Framework.

Napisz mi prosty test, który sprawdza:
1. status 200,
2. że response.data jest listą.

Dodaj komentarze po polsku. Nie używaj bazy danych.
```

---

## 18. Pomoc przy teście POST

Użyj dla testu poprawnego tworzenia obiektu.

```text
Chcę napisać test endpointu:

POST /api/tasks/

Poprawny payload:

WKLEJ_TUTAJ_PAYLOAD

Napisz test z APIClient, który sprawdza:
1. status 201,
2. pole title,
3. pole status,
4. pole priority,
5. obecność id w odpowiedzi.

Komentarze w kodzie po polsku.
```

---

## 19. Pomoc przy teście błędnych danych

Użyj dla testu `400 Bad Request`.

```text
Chcę przetestować walidację w endpointcie:

POST /api/tasks/

Błędny payload:

WKLEJ_TUTAJ_PAYLOAD

Napisz test, który sprawdza:
1. status 400,
2. że w response.data znajduje się pole z błędem,
3. że test nie sprawdza zbyt dokładnie angielskiego tekstu błędu.

Wyjaśnij krótko, dlaczego lepiej sprawdzać obecność pola niż cały tekst komunikatu.
```

---

## 20. Debugowanie testów API

Użyj, gdy test nie przechodzi.

```text
Mam test API w pytest:

WKLEJ_TUTAJ_TEST

Test nie przechodzi. Oto błąd:

WKLEJ_TUTAJ_BŁĄD

Pomóż mi zdebugować:
1. czy problem jest w URL-u,
2. czy problem jest w statusie HTTP,
3. czy problem jest w danych wejściowych,
4. czy problem jest w serializerze,
5. czy problem jest w konfiguracji pytest-django.

Nie generuj całego projektu. Prowadź mnie krok po kroku.
```

---

## 21. Review testów endpointów

Użyj, gdy chcesz sprawdzić jakość testów.

```text
Oto moje testy endpointów DRF:

WKLEJ_TUTAJ_KOD_TESTOW

Oceń:
1. czy testuję happy path,
2. czy testuję błędne dane,
3. czy testy są czytelne,
4. czy nazwy testów są dobre,
5. czy czegoś ważnego brakuje.

Zaproponuj maksymalnie 5 konkretnych poprawek.
```

---

# 📝 Dokumentacja API

## 22. Pomoc przy dokumentacji API

Użyj, gdy chcesz szybko przygotować prostą dokumentację w README.

```text
Mam endpointy:

GET /api/tasks/
POST /api/tasks/

Pola obiektu Task:
- id,
- title,
- description,
- status,
- priority.

Przygotuj krótką dokumentację API w Markdown.

Dokumentacja ma zawierać:
- opis endpointu,
- metodę HTTP,
- przykład requestu,
- przykład response,
- statusy sukcesu,
- status błędu walidacji.

Nie używaj Swaggera ani OpenAPI. To ma być prosta dokumentacja w README.
```

---

## 23. Review dokumentacji API

Użyj, gdy masz już opis API i chcesz sprawdzić, czy jest przydatny.

```text
Oto moja dokumentacja API:

WKLEJ_TUTAJ_DOKUMENTACJE

Sprawdź:
1. czy endpointy są jednoznaczne,
2. czy przykłady requestów są poprawne,
3. czy response zawiera sensowne dane,
4. czy statusy HTTP są poprawne,
5. czy frontend developer wiedziałby, jak użyć tego API.

Zaproponuj krótkie poprawki.
```

---

# 🧩 Capstone

## 24. Pomoc przy capstone

Użyj, gdy dopiero wybierasz domenę projektu końcowego.

```text
Buduję projekt końcowy kursu AI Python Engineer.

Moja domena to:

OPISZ_DOMENE

Chcę po weekendzie Django mieć:
- projekt Django,
- aplikację domenową,
- endpoint /health/,
- pierwszy serializer,
- GET listy obiektów,
- POST tworzenia obiektu,
- testy API.

Pomóż mi dobrać:
1. nazwę aplikacji Django,
2. główną encję,
3. 5 pól encji,
4. dozwolone statusy lub kategorie,
5. nazwy endpointów REST.
```

---

## 25. Dopasowanie domeny capstone do serializerów

Użyj, gdy masz domenę i chcesz z niej zrobić pierwszy serializer.

```text
Moja aplikacja capstone dotyczy:

OPIS_DOMENY

Zaproponuj serializer DRF dla pierwszej encji biznesowej.

Warunki:
- użyj serializers.Serializer,
- nie używaj jeszcze ModelSerializer,
- dodaj minimum jedno ChoiceField,
- dodaj minimum jedno pole opcjonalne,
- nazwy pól po angielsku,
- komentarze po polsku tylko tam, gdzie naprawdę pomagają.
```

---

## 26. Checklist jakości przed commitem

Użyj przed zrobieniem commita.

```text
Przed commitem mojego projektu Django sprawdź checklistę jakości.

Mój aktualny stan:
- endpoint /health/: TAK/NIE
- GET /api/tasks/: TAK/NIE
- POST /api/tasks/: TAK/NIE
- serializer: TAK/NIE
- test GET: TAK/NIE
- test POST success: TAK/NIE
- test validation error: TAK/NIE
- pytest przechodzi: TAK/NIE

Na podstawie tej listy powiedz:
1. co jest gotowe,
2. co blokuje commit,
3. co mogę poprawić później,
4. jaki komunikat commita będzie dobry.
```

---

# 🎓 Nauka i rozmowa techniczna

## 28. Prompt do nauki, nie do kopiowania

Użyj jako quiz po weekendzie.

```text
Zadaj mi 8 pytań sprawdzających, czy rozumiem Django po tym weekendzie.

Zakres:
- projekt vs aplikacja,
- settings.py,
- urls.py,
- views.py,
- serializers.py,
- APIView,
- ViewSet,
- statusy HTTP,
- testy API.

Po każdym moim wyborze daj krótkie wyjaśnienie.
Nie dawaj od razu wszystkich odpowiedzi.
```

---

## 29. Prompt do symulacji rozmowy technicznej

Użyj, gdy chcesz sprawdzić gotowość do rozmowy junior Python/Django developer.

```text
Przeprowadź ze mną krótką symulację rozmowy technicznej na junior Python/Django developer.

Temat:
Pierwsze API w Django REST Framework.

Zadawaj pytania pojedynczo. Po mojej odpowiedzi oceń ją krótko i dopytaj. Po 8 pytaniach podsumuj:
- co rozumiem dobrze,
- co muszę powtórzyć,
- jakie 3 ćwiczenia powinienem zrobić.
```

---

## 30. Prompt do refaktoryzacji bez przesady

Użyj, gdy chcesz poprawić kod, ale nie chcesz wyjść poza poziom zajęć.

```text
Oto mój kod Django z weekendu 5:

WKLEJ_TUTAJ_KOD

Zaproponuj drobne refaktoryzacje, ale bez wprowadzania:
- modeli Django,
- bazy danych,
- autoryzacji,
- permissions,
- pagination,
- zaawansowanych klas DRF.

Chcę zachować poziom początkujący i dobrze zrozumieć każdą zmianę.
```

---

## 32. Prompt do przygotowania zadania domowego

Użyj, gdy chcesz rozbudować projekt po zajęciach.

```text
Na podstawie mojego obecnego API:

WKLEJ_TUTAJ_OPIS_ENDPOINTOW

Zaproponuj zadanie domowe na 2–3 godziny, które rozbuduje projekt, ale nie wymaga jeszcze bazy danych.

Zadanie ma zawierać:
- opis biznesowy,
- wymagania funkcjonalne,
- wymagania techniczne,
- listę testów,
- kryteria akceptacji,
- wersję podstawową i ambitniejszą.
```

---

## 35. Prompt do przygotowania się na kolejny blok

Użyj po weekendzie jako powtórkę przed modelami, bazą i ORM.

```text
Po weekendzie Django znam:
- projekt i aplikacje Django,
- routing,
- views,
- templates light,
- serializers,
- APIView,
- ViewSet,
- routers,
- testy API.

Przygotuj mi listę rzeczy, które powinienem powtórzyć przed kolejnym blokiem o modelach, bazie danych i ORM.

Podziel na:
- konieczne,
- warto umieć,
- dla chętnych.

Dodaj krótkie minićwiczenia.
```

---

# ⛔ Antyprompty — czego unikać

Nie używaj promptów typu:

```text
Napisz mi cały backend Django z API, testami, bazą, autoryzacją, Dockerem i AI.
```

---

## Dlaczego to zły prompt?

Bo prawdopodobnie dostaniesz:

- za dużo kodu naraz,
- kod wykraczający poza aktualny poziom,
- technologie, których jeszcze nie omawialiśmy,
- trudny debugging,
- projekt, którego nie umiesz utrzymać,
- błędy importów, konfiguracji i zależności.

---

## Lepszy prompt

```text
Mam działający endpoint GET /api/tasks/.
Pomóż mi dodać POST krok po kroku z serializerem i walidacją.
Po każdym kroku wyjaśnij, co sprawdzić.
```

---

# ✅ Mini-checklista użycia AI

Przed zaakceptowaniem odpowiedzi AI sprawdź:

```text
[ ] Czy rozumiem każdy import?
[ ] Czy rozumiem każdą klasę?
[ ] Czy kod pasuje do poziomu zajęć?
[ ] Czy kod nie dodaje nieomawianych technologii?
[ ] Czy endpoint działa ręcznie?
[ ] Czy mam test sukcesu?
[ ] Czy mam test błędu?
[ ] Czy statusy HTTP są poprawne?
[ ] Czy potrafię wyjaśnić ten kod komuś innemu?
```

---

## Checklist w wersji Markdown

- [ ] Rozumiem każdy import.
- [ ] Rozumiem każdą klasę.
- [ ] Kod pasuje do poziomu zajęć.
- [ ] Kod nie dodaje nieomawianych technologii.
- [ ] Endpoint działa ręcznie.
- [ ] Mam test sukcesu.
- [ ] Mam test błędu.
- [ ] Statusy HTTP są poprawne.
- [ ] Potrafię wyjaśnić ten kod komuś innemu.

---

# 🧠 Najważniejsza zasada

AI ma pomagać szybciej zrozumieć problem, a nie ukrywać brak zrozumienia.

Po tym weekendzie powinieneś/powinnaś umieć samodzielnie wyjaśnić:

```text
request -> urls.py -> view -> serializer -> response
```

Jeżeli potrafisz to wytłumaczyć na własnym kodzie, jesteś na dobrej drodze do dalszej pracy z Django, DRF i capstone.

> [!IMPORTANT]  
> AI może pomóc Ci znaleźć błąd.  
> Ale to Ty musisz rozumieć, dlaczego poprawka działa.
