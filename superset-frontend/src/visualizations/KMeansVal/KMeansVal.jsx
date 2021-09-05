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
     clusters: PropTypes.array
 };
 const defaultProps = {
     className: '',
     height: 200,
     width: 200,
     idx: [],
     clusters: [],
 };
 
 
 function KMeansVal({
     className,
     height,
     width,
     idx,
     clusters
   }) {
 
    const categories = idx.map(r=> `clust ${r}`);
    const seriesData = clusters.map((row, rowNum)=>{
        return {
            name: `cluster ${rowNum}`,
            type: 'scatter',
            emphasis: {
                focus: 'series'
            },
            data: row
        }
    });

     const echartOptions = {
        grid: {
            left: '3%',
            right: '7%',
            bottom: '7%',
            containLabel: true
        },
        tooltip: {
            // trigger: 'axis',
            showDelay: 0,
            formatter: function (params) {
                return params.seriesName;
            }
        },
        toolbox: {
            feature: {
                dataZoom: {},
                brush: {
                    type: ['rect', 'polygon', 'clear']
                }
            }
        },
        legend: {
            data: categories,
            left: 'center',
            bottom: 10
        },
        xAxis: [
            {
                type: 'value',
                scale: true,
                splitLine: {
                    show: false
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                scale: true,
                splitLine: {
                    show: false
                }
            }
        ],
        series: seriesData
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
 