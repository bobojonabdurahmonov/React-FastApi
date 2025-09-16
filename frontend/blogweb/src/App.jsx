import { useState, useEffect } from "react";
import Blogs from "./components/blogs";

function App() {
  const [blogblock, setBlogBLock] = useState(false);

  const toBlog = () => {
    setBlogBLock(prev => !prev);
  };

  useEffect(() => {
    if (blogblock) {
      document.title = "Home";
    } else {
      document.title = "Blogs";
    }
  }, [blogblock]);

  return (
    <div>
      {blogblock ? (
        <>
          <Blogs blog="Welcome to world" />
          <button onClick={toBlog}>Go Home</button>
        </>
      ) : (
        <>
        <h1>Hello World</h1>
        <button onClick={toBlog}>Go to Blogs</button>
        </>
      )}
    </div>
  );
}

export default App;
