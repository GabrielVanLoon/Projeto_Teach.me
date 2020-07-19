import React from 'react';
import './CardProposta.css';

import  { useState } from 'react'

function CardProposta(props) {

    const [collapseState, setCollapseState] = useState(true);
    
    let collapseDiv = React.useRef();

    if(collapseDiv.current){
        collapseDiv.current.style.height =  (collapseState) ? '0px' : collapseDiv.current.scrollHeight+'px';
    }

    function updateCollabseState(){
        setCollapseState( !collapseState );
    }

    function renderAula(item){
        return (
            <tr>
                <td>#{item.lesson_number}</td>
                <td>{item.start}</td>
                <td>{item.place}</td>
                <td>R$ {item.full_price}</td>
                <td>{item.status}</td>
            </tr>
        )
    }


    return (
    <article class="card-proposta">
        <table class="dados-propostas">
            <thead>
                <tr class="row-header">
                    <th>Código</th>
                    <th>@Turma</th>
                    <th>@Instrutor</th>
                    <th>Disciplina</th>
                    <th>Status</th>
                    { (collapseState) && 
                        <th><button onClick={ updateCollabseState } class="btn-collapse fa-fw fas fa-chevron-down" title="Ver mais detalhes"></button></th>
                    }
                    { (!collapseState) && 
                        <th><button onClick={ updateCollabseState } class=" btn-collapse fa-fw fas fa-chevron-up" title="Esconder detalhes"></button></th>
                    }
                </tr>
            </thead>
            <tbody>
                <tr class="row">
                <td>#{props.codigo}</td>
                    <td>@{props.turma}</td>
                    <td>@{props.instrutor}</td>
                    <td>{props.disciplina}</td>
                    <td>{props.status}</td>
                </tr>
            </tbody>
        </table>
        
        <div className='collapse' ref={ collapseDiv } style={{height: '0px'}}>
            <table class="dados-aulas">
                <thead>
                    <tr>
                        <th>Aula nº</th>
                        <th>Data e Hora</th>
                        <th>Local</th>
                        <th>Valor Aula</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    { props.aulas.map( renderAula ) }
                </tbody>
            </table>
        </div>

        <table class="iteracoes">
                <tbody>
                    <tr>
                        { (props.status == 'EM APROVAÇÃO' && !props.aceito) &&
                            <td>
                                <button class="btn btn-success"><i class="fa-fw fas fa-check"></i> Aceitar Proposta</button>
                                <button class="btn btn-danger"><i class="fa-fw fas fa-times"></i> Recusar Proposta</button>
                                <button class="btn"><i class="fa-fw fas fa-share"></i> Ver Turma</button>
                            </td>
                        }

                        { !(props.status == 'EM APROVAÇÃO' && !props.aceito) &&
                            <td>
                                <button class="btn"><i class="fa-fw fas fa-share"></i> Ver Turma</button>
                            </td>
                        }

                    </tr>
                </tbody>
            </table>
    </article>
    );
}

export default CardProposta;