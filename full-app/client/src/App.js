import './App.css';
import { useState, useEffect } from 'react';
import ArticleList from './components/ArticleList';

function App() {

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

    return (
        <div className="App">
            <h1>Flash and ReactJS</h1>
            <ArticleList articles = {articles}/>
        </div>
    );
}

export default App;
