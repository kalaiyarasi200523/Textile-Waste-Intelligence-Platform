import{ useState } from "react";
import './App.css';

function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("");

  const registerUser = async () => {
    console.log("Register button clicked");
  const response = await fetch("http://127.0.0.1:8000/users/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: username,
      password: password,
      role: role,
    }),
  });
  console.log(response.status);
  

  const data = await response.json();
  console.log(data);
  alert(JSON.stringify(data));
};


  return (
    <div className="container">
      <h1>Textile Waste Intelligence Platform</h1>

      <h2>Login</h2>

      <input 
  type="text"
  placeholder="Username"
  value={username}
  onChange={(e) => setUsername(e.target.value)}
/>
      <br /><br />

      <input type="password" placeholder="Password"
  value={username}
  onChange={(e) => setUsername(e.target.value)}
 />
      <br /><br />

      <button>Login</button>

      <hr />

      <h2>Register</h2>
      
      <input 
      type="text"
       placeholder="Username" 
      value={username} 
      onChange={(e) => 
      setUsername(e.target.value)} />

      
      <br /><br />

      
      <input 
      type="Password"
       placeholder="Password" 
      value={password} 
      onChange={(e) => 
      setPassword(e.target.value)} />
      <br /><br />

      <input 
      type="text"
       placeholder="role" 
      value={role} 
      onChange={(e) => 
      setRole(e.target.value)} />
      

      <button onClick={registerUser}>
        Register</button>

      <hr />

      <h2>Inventory</h2>

      <input type="text" placeholder="Waste Batch ID" />
      <br /><br />

      <input type="text" placeholder="Fabric Type" />
      <br /><br />

      <input type="text" placeholder="Source" />
      <br /><br />

      <input type="text" placeholder="Quantity" />
      <br /><br />

      <input type="text" placeholder="Color" />
      <br /><br />

      <input type="text" placeholder="Condition" />
      <br /><br />

      <input type="date" />
      <br /><br />

      <button>Add Inventory</button>
    </div>
  );
}

export default App;
