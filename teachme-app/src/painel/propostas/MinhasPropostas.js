import React from 'react';
import API from "../../utils/API";
import { useState, useRef, useEffect } from "react";
import './MinhasPropostas.css';

import { Router, Link , navigate } from "@reach/router"

import CardProposta from './CardProposta'


function MinhasTurmas(props) {

    if(!localStorage.getItem('username')){
        navigate(`/login`)
    }

    const [status, setStatus] = useState(''); 
    const [resultados, setResultados] = useState([]); 
    const [nroResultados, setNroResultados]   = useState(0);


    function buscarResultados(){
        let data = `username=${localStorage.getItem('username')}&status=${status}`

        API.post('proposals', data, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }} )
        .then(response => {
            setNroResultados(response.data.rows)
            setResultados(response.data.proposals)
        })
        .catch(error => {
            // alert('Erro de Conexão!')
        });
    }

    useEffect(() => {
        buscarResultados()
    }, [status]);


    function renderProposta(item){

        return (
            <CardProposta id={item.id} turma={item.classname} instrutor={item.instructor} disciplina={item.subject}
                codigo={item.code} status={item.status} dataCriacao={item.creation_date} 
                precoTotal={item.full_price} aceito={item.accept} aulas={item.lessons}/>
        )
    }

    return(
        <main id="page-minhas-propostas" class="body-card">
            <h1>Aulas e Propostas</h1>

            <section class="filtros">
                <label for="filtro-status">Filtrar propostas </label>
                <select id="filtro-status" name="filtro-status"
                    value={status} onChange={e => setStatus(e.target.value)}>
                    <option value=''>Mostrar todas</option>
                    <option value='EM APROVAÇÃO'>Em Aprovação</option>
                    <option value='APROVADA'>Em andamento</option>
                    <option value='RECUSADA'>Recusadas</option>
                    <option value='FINALIZADA'>Finalizadas</option>
                </select>
            </section> 

            <section class="propostas">
                { resultados.map( renderProposta ) }
            </section>

        </main>
    );
}

export default MinhasTurmas;