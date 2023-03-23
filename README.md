# Generator kalendarzy WEiTI

## Instalacja
```console
    git clone git@github.com:jkowalc/weiti-calendar-generator.git
    cd weiti-calendar-generator
    pip install -r requirements.txt
```
## Uruchomienie
```console
    PYTHONPATH="." python3 src/main.py
```
## Import kalendarza do aplikacji
Program wygeneruje kalendarz w formacie iCalendar (.ics) do pliku `calendar.ics`.  
Można go zaimportować do praktycznie dowolnej aplikacji, np. Google Calendar, Outlook, Thunderbird, etc.  

### Google Calendar, Outlook
Odsyłam do dokumentacji [Microsoftu](https://support.microsoft.com/pl-pl/office/importuj-kalendarze-do-programu-outlook-8e8364e1-400e-4c0f-a573-fe76b5a2d379), [Google](https://support.google.com/calendar/answer/37118?hl=pl&co=GENIE.Platform%3DDesktop).

### Thunderbird

1. Open the "Today Pane" ie. the Events panel on the right hand side next to the email list.
2. Drag&Drop the ics-file onto that pane.

N.B In Windows 7, you need to hold the CTRL key down while dragging the ICS file on to the events pane.  
*[Źródło](https://superuser.com/questions/382022/how-do-i-get-thunderbird-to-open-an-ics-attachment-directly-in-lightnings-calen)*
