/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
 import React from 'react';
 import Echart from '@superset-ui/plugin-chart-echarts/lib/components/Echart'
 import PropTypes from 'prop-types';
 
 
 const propTypes = {
     className: PropTypes.string,
     height: PropTypes.number,
     width: PropTypes.number,
     idx: PropTypes.array,
     euclidean: PropTypes.array
 };
 const defaultProps = {
     className: '',
     height: 200,
     width: 200,
     idx: [],
     euclidean: [],
 };
 
 
 function KMeansVal({
     className,
     height,
     width,
     idx,
     euclidean
   }) {
 
     const echartOptions = {
         xAxis: {
             name: '簇数',
             type: 'category',
             data: idx
         },
         yAxis: {
             name: '欧氏距离',
             type: 'value',
             scale: true
         },
         series: [{
             data: euclidean,
             type: 'line'
         }],
         tooltip: {
             trigger: 'axis',
             formatter: (data)=>{
                 console.log(data)
                 return `num_cluster: ${data[0].value}`
             }
         },
     };
 
 
     return (
         <Echart
             className={className}
             height={height}
             width={width}
             echartOptions={echartOptions}
             // eventHandlers={eventHandlers}
             // selectedValues={selectedValues}
         />
     );
 }
 
 
 KMeansVal.propTypes = propTypes;
 KMeansVal.defaultProps = defaultProps;
 
 export default KMeansVal;
 