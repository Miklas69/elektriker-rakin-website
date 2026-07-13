<?php
/*
 * Kontaktformular-Backend — Elektrotechnik Rakin OHG
 * ---------------------------------------------------
 * STATUS: vorbereitet, NOCH NICHT AKTIV.
 * Die Website läuft aktuell im Demo-Modus (handleSubmit zeigt nur die
 * Erfolgsmeldung, sendet nichts). Siehe Übergabe-Doku, Abschnitt 4.
 *
 * AKTIVIERUNG BEI GO-LIVE (3 Schritte):
 *
 * 1) Diese Datei auf den Hoster (PHP nötig, z.B. All-Inkl) hochladen.
 *
 * 2) In index.html die Formularfelder mit name-Attributen versehen —
 *    aktuell hat KEIN Feld ein name-Attribut, ohne die wird nichts übertragen:
 *      <input type="text" name="name"     ...>   (Name *)
 *      <input type="tel"  name="phone"    ...>   (Telefon *)
 *      <select            name="leistung" ...>   (Leistung)
 *      <textarea          name="message"  ...>   (Nachricht)
 *      <input type="checkbox" name="consent" ...> (Einwilligung *)
 *
 * 3) In index.html handleSubmit() ersetzen durch:
 *      async function handleSubmit(e) {
 *        e.preventDefault();
 *        const res = await fetch('kontakt.php', {
 *          method: 'POST',
 *          body: new FormData(e.target)
 *        });
 *        const data = await res.json();
 *        if (data.ok) { e.target.reset(); document.getElementById('form-ok').classList.remove('hidden'); }
 *        else { alert('Senden fehlgeschlagen: ' + (data.error || 'Bitte rufen Sie uns an.')); }
 *      }
 *
 * EMPFEHLUNG: Das Formular hat kein E-Mail-Feld. Rakin kann Anfragen nur
 * telefonisch beantworten. Ein optionales Feld <input type="email" name="email">
 * würde die Rückmeldung erleichtern — dieses Skript verarbeitet es bereits,
 * wenn es vorhanden ist.
 */

header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    exit(json_encode(['ok' => false, 'error' => 'Methode nicht erlaubt']));
}

// Eingaben säubern
$name     = trim(strip_tags($_POST['name']     ?? ''));
$phone    = trim(strip_tags($_POST['phone']    ?? ''));
$leistung = trim(strip_tags($_POST['leistung'] ?? ''));
$message  = trim(strip_tags($_POST['message']  ?? ''));
$consent  = isset($_POST['consent']) && $_POST['consent'] !== '';

// E-Mail ist optional (Feld existiert aktuell nicht im Formular)
$emailRaw = trim($_POST['email'] ?? '');
$email    = $emailRaw !== '' ? filter_var($emailRaw, FILTER_VALIDATE_EMAIL) : '';

// Pflichtfelder wie im Formular: Name, Telefon, Einwilligung
if ($name === '' || $phone === '' || !$consent) {
    http_response_code(422);
    exit(json_encode(['ok' => false, 'error' => 'Bitte Name, Telefon und Einwilligung ausfüllen.']));
}
if ($emailRaw !== '' && $email === false) {
    http_response_code(422);
    exit(json_encode(['ok' => false, 'error' => 'Die E-Mail-Adresse ist ungültig.']));
}
if (mb_strlen($message) > 5000) {
    http_response_code(422);
    exit(json_encode(['ok' => false, 'error' => 'Nachricht zu lang.']));
}

$to      = 'Service@Elektrotechnik-Rakin.de';
$subject = '=?UTF-8?B?' . base64_encode('Neue Anfrage über die Website von ' . $name) . '?=';

$body  = "Name:     $name\n";
$body .= "Telefon:  $phone\n";
if ($email)    { $body .= "E-Mail:   $email\n"; }
if ($leistung) { $body .= "Leistung: $leistung\n"; }
$body .= "\nNachricht:\n" . ($message !== '' ? $message : '(keine Nachricht angegeben)');
$body .= "\n\n--\nGesendet über das Kontaktformular auf elektrotechnik-rakin.de";

// From muss eine Adresse der eigenen Domain sein (sonst SPF/DMARC-Ablehnung)
$headers  = "From: website@elektrotechnik-rakin.de\r\n";
$headers .= 'Reply-To: ' . ($email ?: $to) . "\r\n";
$headers .= "Content-Type: text/plain; charset=utf-8\r\n";

$sent = mail($to, $subject, $body, $headers);

if (!$sent) {
    http_response_code(500);
    exit(json_encode(['ok' => false, 'error' => 'Versand fehlgeschlagen. Bitte rufen Sie uns an: 0160 9162 8756']));
}

echo json_encode(['ok' => true]);
