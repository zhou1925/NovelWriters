import axios from 'axios';
import React, { useState, useEffect } from 'react';
import Chapter from './Chapter';


function Novel({ match, history }) {
  const [novel, setNovel] = useState([]);
  const [author, setAuthor] = useState("");
  const [chapters, setChapters] = useState([]);

  useEffect(() => {
      async function fetchData() {
          const novel = await axios.get(`http://localhost:8000/api/novels/${match.params.id}`);
          setNovel(novel.data);
          setChapters(novel.data.chapters);
          setAuthor(novel.data.author.username);
      }
      fetchData();
  }, [])
    return (
        <div>
          <div className="w-full mx-auto lg:w-4/5">
            <h1 className="flex items-center text-center font-sans font-bold break-normal text-gray-900 px-2 text-5xl">
				      {novel.title}
            </h1>
            <h2 className="font-sans font-medium break-normal text-gray-500 px-2 pb-2 text-2xl">Novel description</h2>
            <div className="p-8 mt-6 lg:mt-0 leading-normal rounded shadow bg-white">
                <p className="font-light">{novel.description}</p>
            </div>
            {chapters && chapters.map((chapter, index) => {
              return (
                <div className="align-middle mx-auto border bg-red">
                <Chapter
                key={index}
                title={chapter.title}
                body={chapter.body}
                />
                </div>
              )
            })}        
          </div>
          <div className="mx-auto w-full text-center items-center mt-6 mb-6">
            <button
            className="bg-transparent hover:bg-blue-500 text-blue-700 
            font-semibold hover:text-white py-2 px-4 border border-blue-500 rounded" 
            onClick={() => history.push('/novels')}>Back Novels</button>
          </div>

        </div>
    )
}

export default Novel;
