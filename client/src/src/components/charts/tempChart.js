import {
    Area,
    AreaChart,
    XAxis,
    YAxis,
    CartesianGrid,
    ResponsiveContainer,
    Tooltip,
    Legend
  } from 'recharts';



const TempChart = ({data}) =>{
    return(
        <div className='temp-chart'>
            <ResponsiveContainer width="80%" height={200}>
            <AreaChart  data={data}>
                <XAxis dataKey="currentDate"/>
                <YAxis dataKey="temperature"/>
                <Tooltip/>
                <Legend verticalAlign="top" height={36}/>
                <Area name="Temperature °C" type="monotone" dataKey="temperature" stroke="#f73636" fill='#f50509'/>
            </AreaChart>
            </ResponsiveContainer>
        </div>
    )
}

export default TempChart;