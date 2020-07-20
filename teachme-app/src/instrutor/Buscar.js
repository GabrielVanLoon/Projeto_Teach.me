import React from 'react';
import API from "../utils/API";
import { useState, useRef, useEffect } from "react";
import './Buscar.css';


function Buscar() {
    
    const [mostrarFiltro, setMostrarFiltro] = useState(false); 

    const [disciplina, setDisciplina] = useState(""); 
    const [cidade,      setCidade]    = useState(""); 
    const [uf, setUF]                 = useState(""); 
    const [semana, setSemana]         = useState(""); 
    const [horario, setHorario]       = useState(""); 
    const [precoMax, setPrecoMax]     = useState(""); 

    const [resultados, setResultados]         = useState([]); 
    const [nroResultados, setNroResultados]   = useState(0);

    function buscarResultados(){
        let data = `subject=${disciplina}&state=${uf}&city=${cidade}`
        data += `&weekday=${semana}&time=${horario}&max_price=${precoMax}`

        API.post('instructors', data, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }} )
        .then(response => {
            setNroResultados(response.data.rows)
            setResultados(response.data.results)
        })
        .catch(error => {
            alert('Erro de Conexão!')
        });
    }

    const handleSubmit = async (evt) => {
        evt.preventDefault()
        buscarResultados()
    } 

    function cardInstrutor(item){
        return(
            <article>
                <div class="picture">
                    {/* <img src="https://oficinadainteligencia.com.br/wp-content/uploads/2019/07/opulent-profile-square-06.jpg"/> */}
                    <img src={process.env.PUBLIC_URL + '/images/instrutora_teachme.jpg'} />
                </div>
                <div class="info">
                    <h3>{ item.name } { item.last_name }</h3>
                    <h4>{ item.degree }</h4>
                    <p>{  item.abstract }</p>
                      
                    { item.subject == '' && 
                        <p class="price"> 
                            <span> Aulas à partir de R$ { item.base_price }</span>
                            <a href="" title={item.username} class="btn">Ver perfil</a>
                        </p>
                    }

                    { item.subject != '' && 
                        <p class="price"> 
                            <span> Aulas de { item.subject }: R$ { item.base_price }/Aula</span>
                            <a href="" title={item.username}  class="btn">Ver perfil</a>
                        </p>
                    }

                </div>
            </article>
        );
    }
    
    return (
        <main id="page-buscar-instrutor" class="body-card">
            <h1>Buscar Instrutores</h1>
            <section class="formulario">
                <form onSubmit={handleSubmit}> 
                    
                    <div class="form-group">
                        <label for="disciplina">Disciplina</label>
                        <select name='disciplina'
                            value={disciplina} onChange={e => setDisciplina(e.target.value)}>
                            <option value=''>Todos</option>
                            <optgroup label="Línguas">
                                <option value='Inglês'>Inglês</option>
                                <option value='Francês'>Francês</option>
                                <option value='Alemão'>Alemão</option>
                            </optgroup>
                            <optgroup label="Computação">
                                <option value='P. O. O.'>P.O.O.</option>
                                <option value='Programação Competitiva'>Programação Competitiva</option>
                                <option value='Banco de Dados'>Banco de Dados</option>
                            </optgroup>
                            <optgroup label="Matemática">
                                <option value='Cálculo'>Cálculo</option>
                                <option value='Estatística'>Estatística</option>
                                <option value='Geometria Analítica'>Geometria Analítica</option>
                            </optgroup>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="uf">UF</label>
                        <select name='uf'
                            value={uf} onChange={e => setUF(e.target.value)}>
                            <option value=''>Todos</option>
                            <option value='SP'>São Paulo</option>
                            <option value='MG'>Minas Gerais</option>
                            <option value='BA'>Bahia</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="cidade">Cidade</label>
                        <select name='cidade' 
                            value={cidade} onChange={e => setCidade(e.target.value)}>
                            <option value=''>Todos</option>

                            { uf == 'SP' &&
                                <optgroup label="SP">
                                    <option value='São Carlos'>São Carlos</option>
                                    <option value='Araraquara'>Araraquara</option>
                                    <option value='Rio Claro'>Rio Claro</option>
                                </optgroup>
                            }

                            { uf == 'BA' &&
                                <optgroup label="BA">
                                    <option value='Alagoinhas'>Alagoinhas</option>
                                </optgroup>
                            }

                            { uf == 'MG' &&
                                <optgroup label="MG">
                                    <option value='Januária'>Januária</option>
                                </optgroup>
                            }

                        </select>
                    </div>

                    <div class="form-group">
                        <button type="submit" class="btn">Buscar</button>
                    </div>
                    
                </form>

                <p class="text-right"><small>
                    <a onClick={e => setMostrarFiltro(!mostrarFiltro)}> Mostrar mais filtros.</a>
                </small></p>

                { mostrarFiltro && 
                    <div class="filters" >
                        
                        <div class="form-group">
                            <label for="semana">Dia da Semana</label>
                            <select name='semana'
                                value={semana} onChange={e => setSemana(e.target.value)}>
                                <option value=''>Todos</option>
                                <option value='SEG'>SEG</option>
                                <option value='TER'>TER</option>
                                <option value='QUA'>QUA</option>
                                <option value='QUI'>QUI</option>
                                <option value='SEX'>SEX</option>
                                <option value='SAB'>SAB</option>
                                <option value='DOM'>DOM</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="semana">Horário</label>
                            <select name='uf'
                                value={horario} onChange={e => setHorario(e.target.value)}>
                                <option value=''>Todos</option>
                                <option value='14:00'>14:00</option>
                                <option value='15:00'>15:00</option>
                                <option value='16:00'>16:00</option>
                                <option value='17:00'>17:00</option>
                                <option value='18:00'>18:00</option>
                            </select>
                        </div>


                        <div class="form-group">
                            <label for="preco-max">Preço Máximo</label>
                            <input type="number" step="0.01" name="preco-max" 
                                value={precoMax} onChange={e => setPrecoMax(e.target.value)}/>
                        </div>

                    </div>
                }

            </section>

            
            <section class="resultados">
                <h3> { nroResultados} instrutores encontrados </h3>
                { resultados.map( cardInstrutor ) }

            </section>
        </main>
    );
}
  
export default Buscar;