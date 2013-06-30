%rebase layout nav_collapse_status='products'

<div class="container">
    <div class="page-header">
<h2> 产品报价 </h2>
<blockquote>
2013-5-31
</blockquote>
</div
<div>

<table border="2">
<tr>
<td>产品名称</td>
<td>规格</td>
<td>包装</td>
<td>产地</td>
<td>数量</td>
<td>单价(元/吨)</td>
<td>交货地点</td>
<tr>
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>
</div>
    <div id="push"></div>
<hr>
</div>

