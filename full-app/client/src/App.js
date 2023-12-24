import './App.css';
import { useState, useEffect } from 'react';
import ArticleList from './components/ArticleList';
import Form from './components/Form';

function App() {

    const [editedArticle, setEditedArticle] = useState(null);
    const [articles, setArticles] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/get', 
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(response => response.json())
        .then(response => 
            setArticles(response)
        )
        .catch((error) => 
            console.error('Error:', error)
        );
    }, []);  
    
    const editArticle = (article) => {
        setEditedArticle(article);
    }

    const updatedData = (article) => {
        const new_article = articles.map(my_article => {
            if (my_article.id === article.id) {
                return article;
            } else {
                return my_article;
            }
        })

        setArticles(new_article);
    }

    const openForm = () => {
        setEditedArticle({title: '', body: ''});
    }

    const insertedArticle = (article) => {
        const new_articles = [...articles, article];
        setArticles(new_articles);
    }

    const deleteArticle = (article) => {
        const new_articles = articles.filter(my_article => {
            if (my_article.id === article.id) {
                return false;
            }
            return true;
        })
        setArticles(new_articles);
    }

    return (
        <div className="App">
            <div className="row">
                <div className="col">
                    <h1>Flask and ReactJS</h1>
                </div>
                <div className="col">
                    <button
                        onClick={openForm}
                        className="btn btn-success float-end"
                    >Add Article</button>
                </div>
            </div>
            <ArticleList 
                articles = {articles}
                editArticle = {editArticle}
                deleteArticle = {deleteArticle}
            />

            {editedArticle ? <Form 
                article = {editedArticle} 
                updatedData = {updatedData} 
                insertedArticle = {insertedArticle}
            /> : null}
        </div>
    );
}

export default App;
