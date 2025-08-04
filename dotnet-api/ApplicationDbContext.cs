using Microsoft.EntityFrameworkCore;

public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
    {
        // Case-insensitive sql statement and column names
        this.ChangeTracker.QueryTrackingBehavior = QueryTrackingBehavior.NoTracking;
        this.ChangeTracker.LazyLoadingEnabled = false;
    }

    public DbSet<User> Users { get; set; }
}