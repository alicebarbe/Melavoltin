import React, {useState, useEffect} from 'react';
import Page from './Page';
import {DataProvider} from './DataContext';

const App = () =>{
  
  return <>
    <DataProvider>
      <Page />
    </DataProvider>
  </>
}

export default App;
