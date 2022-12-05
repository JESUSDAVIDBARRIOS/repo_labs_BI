def crear_tablas():
    return """

        CREATE TABLE IF NOT EXISTS municipio(
            Codigo_entidad DECIMAL PRIMARY KEY,
            Entidad VARCHAR(150),
            Departamento VARCHAR(150)
        );

        CREATE TABLE IF NOT EXISTS hecho_produccion_minera(
            HPM_PKDWH SERIAL PRIMARY KEY,
            Codigo_entidad DECIMAL FOREIGN KEY REFERENCES municipio (Codigo_entidad),
            Recurso_natural VARCHAR(150),
            Año DECIMAL,
            Trimestre VARCHAR(150),
            Valor_contraprestacion DECIMAL
        );

        CREATE TABLE IF NOT EXISTS numPersonasDesplazadas_Conflicto(
            NPD_PKDWH SERIAL PRIMARY KEY,
            Codigo_entidad DECIMAL FOREIGN KEY REFERENCES municipio (Codigo_entidad),
            DatoNumerico DECIMAL,
            Año DECIMAL,
            Mes DECIMAL
        );

        CREATE TABLE IF NOT EXISTS PuntajeSisben_Demografia(
            PSD_PKDWH SERIAL PRIMARY KEY,
            Codigo_entidad DECIMAL FOREIGN KEY REFERENCES municipio (Codigo_entidad),
            DatoNumerico DECIMAL,
            Año DECIMAL,
            Mes DECIMAL
        );


        CREATE TABLE IF NOT EXISTS MDM_desempleo(
            MDM_PKDWH SERIAL PRIMARY KEY,
            Codigo_entidad DECIMAL FOREIGN KEY REFERENCES municipio (Codigo_entidad),
            DatoNumerico DECIMAL,
            Año DECIMAL,
            Mes DECIMAL
        );


         CREATE TABLE IF NOT EXISTS CoberturaAcueducto_vivienda(
            CAV_PKDWH SERIAL PRIMARY KEY,
            Codigo_entidad DECIMAL FOREIGN KEY REFERENCES municipio (Codigo_entidad),
            DatoNumerico DECIMAL,
            Año DECIMAL,
            Mes DECIMAL
        );


         CREATE TABLE IF NOT EXISTS PuntajePromedioICFES_educacion(
            PSD_PKDWH SERIAL PRIMARY KEY,
            Codigo_entidad DECIMAL FOREIGN KEY REFERENCES municipio (Codigo_entidad),
            Indicador VARCHAR(250),
            DatoNumerico DECIMAL,
            Año DECIMAL,
            Mes DECIMAL
        );


         CREATE TABLE IF NOT EXISTS MortalidadNeonatal_salud(
            MNS_PKDWH SERIAL PRIMARY KEY,
            Codigo_entidad DECIMAL FOREIGN KEY REFERENCES municipio (Codigo_entidad),
            DatoNumerico DECIMAL,
            Año DECIMAL,
            Mes DECIMAL
        );


         CREATE TABLE IF NOT EXISTS IPM_pobreza(
            IPM_PKDWH SERIAL PRIMARY KEY,
            Codigo_entidad DECIMAL FOREIGN KEY REFERENCES municipio (Codigo_entidad),
            DatoNumerico DECIMAL,
            Año DECIMAL,
            Mes DECIMAL
        );
    """
