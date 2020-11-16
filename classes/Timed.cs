using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Rentoolo.Model
{
    public st class SellFilter
    {
        public string Search { get; set; }
        public DateTime StartDate { get; set; }
        public DateTime EndDate { get; set; }

        public bool OnlyInName { get; set; }

        public decimal StartPrice { get; set; }
        public decimal EndPrice { get; set; }

        public string City { get; set; }

        public string SortBy { get; set; };
    }
}