# Author: Francisco Senén Gómez Méndez

import os
import sys
import patoolib

def descomprimir_archivos(archivos_comprimidos):
    for archivo_comprimido in archivos_comprimidos:
        try:
            patoolib.extract_archive(archivo_comprimido, outdir=os.getcwd())
            print(f"[+] Archivo '{archivo_comprimido}' descomprimido exitosamente.")
        except Exception as e:
            print(f"[-] Error al descomprimir el archivo '{archivo_comprimido}':", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python autoExtract.py <archivo_comprimido1> <archivo_comprimido2> ...")
        sys.exit(1)

    archivos_comprimidos = sys.argv[1:]
    descomprimir_archivos(archivos_comprimidos)
