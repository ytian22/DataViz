data = [
{
type: 'scatterpolar',
r: [2.0, 2.0, 4.0, 5.0, 4.0, 3.0, 3.0, 3.0, 5.0, 4.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Marina',
},

{
type: 'scatterpolar',
r: [5.0, 5.0, 2.0, 4.0, 3.0, 4.0, 5.0, 5.0, 4.0, 4.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Inner Sunset',
},

{
type: 'scatterpolar',
r: [5.0, 3.0, 3.0, 3.0, 4.0, 3.0, 3.0, 3.0, 4.0, 4.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Inner Richmond',
},

{
type: 'scatterpolar',
r: [4.0, 5.0, 2.0, 5.0, 3.0, 2.0, 2.0, 2.0, 4.0, 4.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Twin Peaks',
},

{
type: 'scatterpolar',
r: [2.0, 2.0, 3.0, 4.0, 2.0, 5.0, 2.0, 2.0, 5.0, 4.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Potrero Hill',
},

{
type: 'scatterpolar',
r: [4.0, 4.0, 4.0, 5.0, 5.0, 2.0, 2.0, 2.0, 4.0, 4.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Presidio Heights',
},

{
type: 'scatterpolar',
r: [3.0, 3.0, 5.0, 4.0, 5.0, 1.0, 5.0, 5.0, 5.0, 4.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Russian Hill',
},
      ];

      layout = {
        title: "Neighborhoods with Resiliency Score 4",
        polar: {
          radialaxis: {
            visible: true,
            range: [0, 5],
          }
        },
      };

      Plotly.plot("myDiv4", data, layout);


    </script>
  </div>
</div>
<!-- score 5 -->
<div class="row">
  <div class="6u 12u$(small)">
    <div id="myDiv5"><!-- Plotly chart will be drawn inside this DIV --></div>
    <script>
      <!-- JAVASCRIPT CODE GOES HERE -->

      data = [
{
type: 'scatterpolar',
r: [5.0, 4.0, 4.0, 5.0, 5.0, 3.0, 4.0, 4.0, 5.0, 5.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Castro/Upper Market',
},

{
type: 'scatterpolar',
r: [4.0, 5.0, 2.0, 5.0, 3.0, 4.0, 4.0, 4.0, 4.0, 5.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Diamond Heights/Glen Park',
},

{
type: 'scatterpolar',
r: [4.0, 5.0, 3.0, 3.0, 2.0, 5.0, 5.0, 5.0, 5.0, 5.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Presidio',
},

{
type: 'scatterpolar',
r: [5.0, 5.0, 2.0, 5.0, 3.0, 5.0, 4.0, 4.0, 3.0, 5.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'West of Twin Peaks',
},

{
type: 'scatterpolar',
r: [4.0, 4.0, 4.0, 5.0, 5.0, 3.0, 4.0, 4.0, 5.0, 5.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Haight Ashbury',
},

{
type: 'scatterpolar',
r: [3.0, 4.0, 4.0, 4.0, 4.0, 2.0, 5.0, 5.0, 5.0, 5.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Pacific Heights',
},

{
type: 'scatterpolar',
r: [3.0, 5.0, 2.0, 4.0, 2.0, 3.0, 5.0, 5.0, 2.0, 5.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Seacliff',
},

{
type: 'scatterpolar',
r: [5.0, 4.0, 3.0, 5.0, 4.0, 3.0, 5.0, 5.0, 5.0, 5.0],
theta: ['Hazard Risk', 'Environmental', 'Transportation', 'Community', 'Public Realm', 'Housing Resiliency', 'Economy', 'Health', 'Demographic', 'Resiliency Score'],
fill: 'toself',
name: 'Noe Valley',
},
      ];

      layout = {
        title: "Neighborhoods with Resiliency Score 5",
        polar: {
          radialaxis: {
            visible: true,
            range: [0, 5],
          }
        },
      };

      Plotly.plot("myDiv5", data, layout);