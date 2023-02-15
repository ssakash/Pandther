param([string]$u)

# Uncomment if you need to use headers in your GET request
#$headers = @{ "Authorization" = "Bearer MyAccessToken" }
$url = $u
$response = Invoke-RestMethod -Uri $url -Method Get -Headers $headers
Write-Output $response
