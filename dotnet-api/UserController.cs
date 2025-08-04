using Microsoft.AspNetCore.Mvc;

[Route("api/[controller]")]
[ApiController]
public class UserController : ControllerBase
{
    private readonly IUserRepository _userRepository;

    public UserController(IUserRepository userRepository)
    {
        _userRepository = userRepository;
    }
    
    [HttpGet]
    [Route("users")]
    public async Task<ActionResult> Get()
    {
        return Ok(await _userRepository.GetAll());
    }

    [HttpPost]
    [Route("create")]
    public async Task<ActionResult> Create([FromBody] User user)
    {
        // Validate the user object
        if (user == null || string.IsNullOrEmpty(user.Username) || string.IsNullOrEmpty(user.Email))
        {
            return BadRequest("Invalid user data.");
        }

        try
        {
            var createdUser = await _userRepository.Create(user);
            return Ok(createdUser);
        }
        catch (Exception ex)
        {
            return StatusCode(StatusCodes.Status500InternalServerError, ex.Message);
        }
    }

}