import axios from 'axios';
import { Link } from 'react-router-dom';
import React, { useState, useEffect } from 'react';

function NovelList() {
    const [isLoading, setIsLoading] = useState(true);
    const [novels, setNovels] = useState([]);

    useEffect(() => {
        async function fetchData() {
            const novels = await axios.get('http://localhost:8000/api/novels/');
            setNovels(novels.data.results);
            setIsLoading(false);
        }
        fetchData();
    }, [])

    return (
        <div>
            {isLoading && 
            <div class="fixed top-0 right-0 h-screen w-screen z-50 flex justify-center items-center">
              <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-blue-400"></div>
            </div>
            }
            <div className="antialiased font-sans bg-gray-200">
              <div className="container mx-auto px-4 sm:px-8">
                    <div className="py-8">
                      <div>
                          <h2 className="text-2xl font-semibold leading-tight">Novels</h2>
                      </div>
                      <div className="-mx-4 sm:-mx-8 px-4 sm:px-8 py-4 overflow-x-auto">
                          <div className="inline-block min-w-full shadow rounded-lg overflow-hidden">
                              <table className="min-w-full leading-normal">
                                  <thead>
                                      <tr>
                                          <th className="px-5 py-3 bg-gray-100 text-left text-gray-600 uppercase">
                                            Title
                                          </th>
                                          <th className="px-5 py-3 bg-gray-100 text-left text-gray-600 uppercase">
                                            Author
                                          </th>
                                          <th className="px-5 py-3 bg-gray-100 text-left text-gray-600 uppercase">
                                            Chapters
                                          </th>
                                      </tr>
                                  </thead>
                                  <tbody>
                                    {novels && novels.map((novel, index) => (                    
                                      <tr key={index}>
                                          <td className="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                                              <div className="flex items-center">
                                                  <div className="ml-1">
                                                      <p className="text-gray-900 hover:text-blue-400 whitespace-no-wrap">
                                                        <Link to={`/novels/${novel.id}`}>{novel.title}</Link>
                                                      </p>
                                                  </div>
                                              </div>
                                          </td>
                                          <td className="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                                              <p className="text-gray-900 whitespace-no-wrap">
                                                {novel.author.username}
                                              </p>
                                          </td>
                                          <td className="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                                              <span className="relative inline-block px-3 py-1 font-semibold text-green-900 leading-tight">
                                                  <span aria-hidden className="absolute inset-0 bg-green-200 opacity-50 rounded-full"></span>
                                                  <span className="relative">{novel.chapters.length}</span>
                                              </span>
                                          </td>
                                      </tr>
                                    ))}  
                                  </tbody>
                              </table>
                          </div>
                      </div>
                  </div>
              </div>
            </div>
        </div>
    )
}

export default NovelList;
