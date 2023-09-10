// import React, { useState, useEffect, Fragment } from "react";
// // import Header from "./Header";
// // import Home from "./Home";
// import Post from "./Post";
// import axios from 'axios';

// function App() {

  
//   const API = 'http://127.0.0.1:8000/api/students/';

//   const [allData,setAllData] = useState([]);
//   const [filteredData,setFilteredData] = useState(allData);

//   const handleSearch = (event) =>{
//     let value = event.target.value.toLowerCase();
//     let result = [];
//     console.log("val", value);

//     result = allData.filter( (data) => {
//       return data.name.search(value) != -1;
//     });
//     setFilteredData(result);
//   }

//   useEffect(() => {
//     fetch(API)
//     .then((response) =>  response.json())
//     .then(response => {
//       console.log("response",response)
//       setAllData(response);
//       setFilteredData(response);
//     }) 
//     .catch(error => {
//       console.log('Error getting fake data: ' + error);
//     })
//   }, []);

//   console.log("filtered data" ,filteredData)


//     return (
//       <Fragment>
//         <div>
//           <label>Search:</label>
//           <input type="text" onChange={(event) =>handleSearch(event)} />
//         </div>
//         <div>
//         {filteredData.map((item,i)=>{
//             return(
//               <div>
//                 <div key={i}>
//                   {item.name} {item.email} {item.phone} {item.document}
//                 </div>
//               </div>
//             )
//         })}
//         </div>
//         <Post/>
//       </Fragment>
//     );
//   }


// export default App;
