import { useEffect, useState } from "react"

export default function Blogs() {
    const [blogs, setBlogs] = useState({ allblogs: [] })
    
    const fetchBlog = async () => {
        let request = await fetch("http://127.0.0.1:8000/api/blogs")
        let result = await request.json()
        console.log("API result:", result)
        setBlogs(result)
    }

    useEffect(() => {
        fetchBlog()
    }, [])

    return (
        <div>
            {blogs.allblogs.map(item => (
                <div key={item.id}>
                    <h1>{item.title}</h1>
                    <p>{item.description}</p>
                </div>
            ))}
        </div>
    )
}
