import React from 'react'

function Chapter({title, body}) {
    return (
        <div>
            <h2 className="font-sans font-bold break-normal text-gray-700 px-2 pb-4 text-xl">{title}</h2>
            <div className="p-8 mt-3 lg:mt-0 leading-normal rounded shadow bg-white">
                <p className="my-2 text-lg text-gray-800">{body}</p>
            </div>
        </div>
    )
}

export default Chapter
