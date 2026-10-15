class Stand:
    def __init__(self, codice, metriquadri, padiglione, prezzo):
        self.codice = codice
        self.metriquadri = metriquadri
        self.padiglione = padiglione
        self.prezzo = prezzo
        self.espositore = None  # Espositore assegnato allo stand

    def get_prezzo(self):
        """Restituisce il prezzo dello stand"""
        return self.prezzo

    def __str__(self):
        stato = "Disponibile" if self.espositore is None else "Occupato"
        return f"Stand {self.codice} - Metri quadri: {self.metriquadri} - Padiglione: {self.padiglione} - Prezzo: {self.get_prezzo()} - Stato: {stato}"


class stand_preseextra(Stand):
    def __init__(self, codice, metriquadri, padiglione, prezzo, prese_extra):
        super().__init__(codice, metriquadri, padiglione, prezzo)
        self.prese_extra = prese_extra

    def get_prezzo(self):
        """Restituisce il prezzo dello stand considerando le prese extra"""
        return self.prezzo * (1+0.07*self.prese_extra)  

    def __str__(self):
        stato = "Disponibile" if self.espositore is None else "Occupato"
        return f"Stand {self.codice} - Metri quadri: {self.metriquadri} - Padiglione: {self.padiglione} - Prezzo: {self.get_prezzo()} - Stato: {stato} - Prese extra: {self.prese_extra}"

class stand_premium(Stand):
    def __init__(self, codice, metriquadri, padiglione, prezzo,posizione):
        super().__init__(codice, metriquadri, padiglione, prezzo)
        self.posizione = posizione

    def get_prezzo(self):
        """Restituisce il prezzo dello stand premium"""
        return self.prezzo * 1.3 

    def __str__(self):
        stato = "Disponibile" if self.espositore is None else "Occupato"
        return f"Stand {self.codice} - Metri quadri: {self.metriquadri} - Padiglione: {self.padiglione} - Prezzo: {self.get_prezzo()} - Stato: {stato} - Posizione: {self.posizione}"

class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.stand = None  # Stand assegnato all'espositore

    def assegna_stand(self, stand):
        """Assegna uno stand all'espositore"""
        self.stand = stand

    def __str__(self):
        stand_info = f"Stand {self.stand.codice}" if self.stand else "Nessuno stand assegnato"
        return f"Espositore {self.codice} - Nome: {self.nome} - Cognome: {self.cognome} - {stand_info}"
    

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.stands = []
        self.espositori = []


    """Aggiungere setter e getter se necessari"""
    # TODO
    def __str__(self):
        return f"Fiera: {self.nome} - Numero di stand: {len(self.stands)} - Numero di espositori: {len(self.espositori)}"

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if 'ST' in parts[0]:
                    if len(parts) == 4:
                        codice, metriquadri, padiglione, prezzo = parts[0], float(parts[1]), parts[2], float(parts[3])
                        stand = Stand(codice, metriquadri, padiglione, prezzo)
                        self.stands.append(stand)
                    elif len(parts) == 5:
                        if parts[4].isdigit():
                            codice, metriquadri, padiglione, prezzo, prese_extra = parts[0], float(parts[1]), parts[2], float(parts[3]), int(parts[4])
                            stand = stand_preseextra(codice, metriquadri, padiglione, prezzo, prese_extra)
                            self.stands.append(stand)
                        else:
                            codice, metriquadri, padiglione, prezzo, posizione = parts[0], float(parts[1]), parts[2], float(parts[3]), parts[4]
                            stand = stand_premium(codice, metriquadri, padiglione, prezzo, posizione)
                            self.stands.append(stand)

                elif 'ES' in parts[0]:
                    codice, nome, cognome = parts[0], parts[1], parts[2]
                    espositore = Espositore(codice, nome, cognome)
                    self.espositori.append(espositore)

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        stand = next((s for s in self.stands if s.codice == codice_stand), None)
        espositore = next((e for e in self.espositori if e.codice == codice_espositore), None)
        if stand is None:
            raise ValueError(f"Stand con codice {codice_stand} non trovato.")
        if espositore is None:
            raise ValueError(f"Espositore con codice {codice_espositore} non trovato.")
        if stand.espositore is not None:
            raise ValueError(f"Stand {codice_stand} è già assegnato all'espositore {stand.espositore.codice}.")
        if espositore.stand is not None:
            raise ValueError(f"Espositore {codice_espositore} ha già uno stand assegnato: {espositore.stand.codice}.")     

        if stand and espositore:
            espositore.assegna_stand(stand)
            stand.espositore = espositore



    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for espositore in self.espositori:
            print(espositore)


    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        return sorted(self.stands, key=lambda s: s.get_prezzo())
