# Issue Finder

Extract issue from gitlab csv and convert in markdown format

## User guide install requirements from txt 

__Install requirements__
```bash 
pip install -r requirements.txt
```

__Run App__
```bash 
python3 app.py
```

Result sample
```txt
{
    "SirioTable": [
        "Migliorare implementazione signal in base alle best practice",
        "Dalla versione Internal build 7.0.1.103[20231117.1] non riusciamo pi\u00f9  a intercettare gli eventi custom che vengono lanciati con un id che non \u00e9 quello che passiamo noi al WebComponent"
    ],
    "SirioTooltip": [
        "Se una tooltip viene mostrata sopra la voce di navigazione di un tab, una parte del tab finisce sopra il tooltip",
        "Il click sul link \u201cAzione\u201d con classe sirio-btn della Tooltip di tipo Popover, non emette alcun sirio event"
    ],
    "SirioRangepicker": [
        "Il SirioRangepicker non si disabilita se passato disabled = true"
    ],
    "SirioPaginator": [
        "La versione smart del SirioPaginator presenta questi due errori in console.\n\nUnhandled Promise rejection: Cannot set properties of null (setting 'currentPage') ; Zone: <root> ; Task: null ; Value: TypeError: Cannot set properties of null (setting 'currentPage') \n\nUncaught (in promise) TypeError: Cannot set properties of null (setting 'currentPage')",
        "Al click sulle frecce di navigazione non viene emesso un sirio event ma viene castato errore: \n\n'Uncaught TypeError: _nav_left._handleclick is not a function at HTMLAnchorElement.onclick'"
    ],
    "SirioValidation": [
        "Se cambio il type del validation, il colore dell'input associato non cambia reattivamente, ma dobbiamo fare refresh della pagina.",
        "Il componente colora del giusto colore l\u2019input, ma nella sezione del testo esce scritto [object promise]. Se ad esempio passo come stringa 'test', il testo della validation sar\u00e1 \"test\" [Object Promise]"
    ],
    "SirioCard": [
        "Se clicco sul sirio-tag, dato che non si tratta di un elemento cliccabile, viene emesso sirioEvent",
        "Nella casistica con type \"link\" passato nel sirio-card, Il click sul tag anchor con classe sirio-card non emette alcun sirio event"
    ],
    "SirioFooter": [
        "La CTA contente l\u2019elemento #ID per l\u2019ancora non emette Sirio Event"
    ],
    "SirioHeader": [
        "In console compare l\u2019errore \u201cHTML element with id=\u201d\u2019sirio-dialog-searchbar-dialog`\" e non si renderizza il componente ma una dialog che ci invita a digitare almeno 3 caratteri \n\nP.S. ( Il problema pare essere collegato a una chiamata CORS )"
    ],
    "SirioAccordion": [
        "Nella versione composed, con codice preso e incollato direttamente dall\u2019esempio della guida senza alcuna manipolazione, ma come provo ad aprire un accordion, questo fa come per aprirsi e si richiude da solo.",
        "Se provo a wrappare l\u2019accordion composed in un componente angular, ricevo errore: Failed to execute 'insertBefore' on 'Node' e non viene renderizzato nulla a video"
    ],
    "SirioTab": [
        "Il caricamento dei nav-items tramite attributo non renderizza le freccette nella versione non composed"
    ],
    "SirioSelect": [
        "Se inserito dentro un componente Tab la select si sdoppia "
    ],
    "SirioInput": [
        "Se inizializzo un input con value = null, poi digito una stringa, e provo a settare tramite javascript il value nuovamente a null, l\u2019input non si aggiorna, se invece inizializzo in unput con value = \"string\", e provo a settare tramite javascript il value = null, l\u2019input si svuota giustamente"
    ],
    "SirioCollapse": [
        "Se inserito in una tab (probabilmente anche in altri), se cliccato fa il glitch come l\u2019accordion light (segnalazione esterna, manca di documentazione)"
    ],
    "InputGroup": [
        "In questo momento il writeValue del componente 'sirio-input-group' non scrive il valore."
    ]
}
```

### Composizione Email
_INFO:_ 
Per andare a capo nel body della email utilizzare la stringa
```NEWLINE```
Aggiungere inoltre tutti i campi richiesti sul _env_sample_

```bash 
TOKEN_GITLAB_PA=
PROJECT_ID=
FILE_REPORT_NAME=

#EMAIL
EMAIL_PORT=
EMAIL_SMTP=
EMAIL_PASSWORD=
EMAIL_USERNAME=
EMAIL_SENDER=
EMAIL_RECIPIENT=
EMAIL_SUBJECT=
EMAIL_BODY=```