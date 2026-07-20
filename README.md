# ALLFJ AI — Invoice Generator

A self-contained invoice editor for **ALLFJ AI**. Single HTML file, no build step,
no dependencies, works offline.

## Use it

Double-click **`index.html`** (opens in your browser). That's it.

- **Left pane** — fill in client, dates, line items, payment details, notes.
  Each line item includes a multiline detailed-description field; line breaks and
  bullet-style lists are preserved in the invoice preview and exported PDF.
- **Right pane** — live A4 preview, updates as you type.
- **Export PDF** — opens the browser print dialog. Choose *Save as PDF*.
  The print output is a clean single A4 page (form/toolbar are hidden).
  In the print dialog, set **Margins: None** and turn **off** "Headers and footers"
  for an edge-to-edge result (the 17 mm inset is built into the sheet).

## What it does

- AUD currency, formatted `A$6,200.00`; amounts = qty × rate, auto subtotal/total.
- GST compliance mode (default on): shows *"GST — Not applicable"* + note.
  Document title is always **"Invoice"**, never "Tax Invoice".
- Auto invoice numbers `ALLFJ-YYYY-NNN` (editable); payment reference tracks the number.
- Saves invoices and reusable clients to your browser's **localStorage**
  (stays on this machine/browser — no server, no cloud).
- Supplier legal name, ABN, email, phone, and the next-number counter live under
  **Supplier & Settings** in the form.

## Notes

- Fonts (Source Serif 4 / IBM Plex Mono) load from Google Fonts when online, with
  serif/mono fallbacks offline. The logo mark is embedded in the file.
- `serve.py` is optional — only needed if you'd rather run it at `http://127.0.0.1:8731`
  (`python3 serve.py`). For everyday use, just open `index.html` directly.
- Data lives in this browser only. To move an invoice to another machine, load it and
  Export PDF, or re-enter it there.
