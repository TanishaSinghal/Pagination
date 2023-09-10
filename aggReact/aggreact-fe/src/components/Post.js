import React,{useState, useEffect, useMemo, useRef, useCallback} from 'react'
// import axios from "axios";
// import { API_URL } from "../constants";

import { AgGridReact } from 'ag-grid-react'; 

import 'ag-grid-community/styles/ag-grid.css'; 
import 'ag-grid-community/styles/ag-theme-alpine.css'; 

const Post = () => {

    const [post, getPost] = useState([])


    // setting up AGGrid states and functions
    // const gridRef = useRef();
    // const [rowData, setRowData] = useState();

    // const [columnDefs, setColumnDefs] = useState([
    //     {field: 'name', filter: true},
    //     {field: 'email', filter: true},
    //     {field: 'document', filter: true},
    //     {field: 'phone', filter: true},
    //     {field: 'registrationDate', filter: true},
    //   ]);

   

    const defaultColDef = useMemo( ()=> ({
        sortable: true
    }));

    // const cellClickedListener = useCallback( event => {
    //     console.log('cellClicked', event);
    // }, []);


    // states and functions for searching/filtering 
    const [allData,setAllData] = useState([]);
    const [filteredData,setFilteredData] = useState(allData);

    const handleSearch = (event) =>{
        let value = event.target.value;
        let result = [];
        console.log("val", value);
        result = allData.filter( (data) => {
            return data.name.search(value) != -1;
        });
        setFilteredData(result);
    }



    // getting up the API
    const API = 'http://127.0.0.1:8000/api/students/';
    const fetchPost = () => {
        fetch(API) 
            .then((res) =>  res.json())
            // .then(res => {
            //     console.log("response",res)
            //     setAllData(res);
            //     setFilteredData(res);
            // }) 
            .then((res) => { 
                console.log(res)
                getPost(res);
                setAllData(res);
                setFilteredData(res);
            }) 
            // .then(rowData => setRowData(rowData))
            
    }

    useEffect( () => {
        fetchPost()
    },[])

    // const buttonListener = useCallback( e => {
    //     gridRef.current.api.deselectAll();
    //   }, []);

    


     // Pagination var hoisting
    //  const [loading, setLoading] = useState(true);
    //  // User is currently on this page
    //  const [currentPage, setCurrentPage] = useState(1);
    //  // No of Records to be displayed on each page   
    //  const [recordsPerPage] = useState(5);
     
   

     
    return(
        <div>

            <div><br /><br />
                <label>Search:</label>
                <input type="text" onChange={(event) =>handleSearch(event)} />
            </div><br /><br />

            <h2>React Fetch Data with DRF API </h2>

            <table className='table'>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Ph.No.</th>
                        <th>Document</th>
                        <th>Registration Date</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        filteredData.map( (item, i) =>{
                            return(<tr>
                                <td>{item.name}</td>
                                <td>{item.email}</td>
                                <td>{item.phone}</td>
                                <td>{item.document}</td>
                                <td>{item.registrationDate}</td>
                            </tr>)
                        })
                    }
                </tbody>
            </table>

            {/* <ul>
                {post.map( (item, i) => {
                    return (
                        <div>
                            <div key={i}> {item.name} {item.email} {item.phone} {item.document}</div>
                        </div>
                    )
                })}
            </ul> */}
           
        
            {/* <h2> AG Grid code </h2>
            <button onClick={buttonListener}>Deselect</button>
            <div className="ag-theme-alpine" style={{width: 1000, height: 500}}>
                <AgGridReact
                    ref={gridRef} // Ref for accessing Grid's API
                    rowData={filteredData} // Row Data for Rows
                    columnDefs={columnDefs} // Column Defs for Columns
                    defaultColDef={defaultColDef} // Default Column Properties
                    rowSelection='multiple' // Options - allows click selection of row
                    onCellClicked={cellClickedListener} // Optional - registering for Grid Event
                />
            </div> */}
            {/* <nav>
                <ul className='pagination'>
                    <li className='page-item'> <button className='page-link' > <i class="bi bi-arrow-left"></i> Previous </button> </li>
                    <li className='page-item'> <button className='page-link' > Next <i class="bi bi-arrow-right"></i></button> </li>

                </ul>
            </nav>    */}



        </div>
    )
}

export default Post