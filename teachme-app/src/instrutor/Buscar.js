import React from 'react';
import './Buscar.css';


const instrutores = [
    {
        nome:      'Maria Joaquina',
        descricao: 'Quisque ac imperdiet dui, quis scelerisque lacus. Vivamus in tortor nunc. Etiam iaculis ut purus sit amet malesuada. Vivamus at odio laoreet, ultrices tellus eu, accumsan sapien. Duis sodales libero quam.',
        preco:     '79,99' 
    }, 
    {
        nome:      'Maria Joaquina',
        descricao: 'Lorem ipsum dolor sit amet veriquas',
        preco:     '79,99' 
    }, 
    {
        nome:      'Maria Joaquina',
        descricao: 'Lorem ipsum dolor sit amet veriquas',
        preco:     '79,99' 
    }, 
]


function Buscar() {
    
    function cardInstrutor(item){
        return(
            <article>
                <div class="picture">
                    <img src="https://oficinadainteligencia.com.br/wp-content/uploads/2019/07/opulent-profile-square-06.jpg"/>
                </div>
                <div class="info">
                    <h3>{ item.nome }</h3>
                    <p>{ item.descricao }</p>
                    <p class="price"><span>Preço: R$ { item.preco }/aula</span><a href="#" class="btn">Ver perfil</a></p>
                </div>
            </article>
        );
    }
    
    return (
        <main id="page-buscar-instrutor" class="body-card">
            <h1>Buscar Instrutor</h1>
            <section class="formulario">
                <form> 
                    
                    <div class="form-group">
                        <label for="disciplina-pai">Área</label>
                        <input type="text" name="disciplina-pai"/>
                    </div>

                    <div class="form-group">
                        <label for="disciplina">Disciplina</label>
                        <input type="text" name="disciplina"/>
                    </div>

                    <div class="form-group">
                        <button type="submit" class="btn">Buscar</button>
                    </div>
                    
                </form>
                <p class="text-right"><small><a href='#'>Configurar filtros.</a></small></p>

                <div class="filters"> 
                    <div class="form-group range-preco">
                        <label for="preco-min">Preço/aula</label>
                        <div>
                            <label for="preco-min">De R$</label>
                            <input type="number" name="preco-min"/>
                            <label for="preco-max">até R$</label>
                            <input type="number" name="preco-max"/>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label for="nome">Nome do Instrutor</label>
                        <input type="text" name="nome"/>
                    </div>
                </div>

            </section>

            
            <section class="resultados">
                <h2>Resultados</h2>
                { instrutores.map( cardInstrutor ) }

            </section>
        </main>
    );
}
  
export default Buscar;